
console.log("APP.JS LOADED");


document.addEventListener("DOMContentLoaded", function () {

    const loading = document.getElementById("loading");
    const result = document.getElementById("result");

    // Hide loading when page opens
    loading.style.display = "none";

    // Keep result visible
    result.style.display = "block";

    console.log("PAGE LOADED");
});


// =========================================
// UPLOAD FILE
// =========================================

async function uploadFile() {

    console.log("UPLOAD BUTTON CLICKED");

    const fileInput = document.getElementById("fileInput");
    const result = document.getElementById("result");
    const loading = document.getElementById("loading");

    if (!fileInput.files.length) {

        alert("Please select a file");

        return;
    }


    const file = fileInput.files[0];

    console.log("Selected file:", file.name);


    const formData = new FormData();

    formData.append("file", file);


    loading.style.display = "block";

    result.style.display = "block";


    result.innerHTML = `
        <div class="file-info">
            <p>
                Analyzing <strong>${file.name}</strong>...
            </p>
        </div>
    `;


    try {

        console.log("Sending file to Flask...");


        const response = await fetch(
            "http://127.0.0.1:5000/api/upload",
            {
                method: "POST",
                body: formData
            }
        );


        console.log("Response status:", response.status);


        const data = await response.json();


        console.log("Server response:", data);


        // DEBUG: Show complete response
        console.log(
            "FINAL DATA:",
            JSON.stringify(data, null, 2)
        );


        console.log("BEFORE SUCCESS CHECK");


        if (!data.success) {

            console.log("SUCCESS IS FALSE");


            result.innerHTML = `
                <div class="error">
                    <p>
                        ${data.message || "Analysis failed."}
                    </p>
                </div>
            `;


            return;
        }


        console.log("SUCCESS IS TRUE");

        console.log("BEFORE DISPLAY RESULTS");


        displayResults(data);


        console.log("AFTER DISPLAY RESULTS");


    } catch (error) {

        console.error("UPLOAD ERROR:", error);


        result.innerHTML = `
            <div class="error">
                <p>
                    Server connection failed.
                </p>
            </div>
        `;


    } finally {

        // Hide ONLY loading
        loading.style.display = "none";


        // Keep result visible
        result.style.display = "block";
        result.style.visibility = "visible";
        result.style.opacity = "1";


        console.log(
            "Loading hidden, result kept visible"
        );
    }
}


// =========================================
// DISPLAY RESULTS
// =========================================

function displayResults(data) {

    console.log("DISPLAY RESULTS CALLED");


    const result = document.getElementById("result");


    let html = `

        <h2>Analysis Results</h2>

        <div class="file-info">

            <p>
                <strong>File:</strong>
                ${data.filename}
            </p>

        </div>

    `;


    // =========================================
    // AI INSIGHTS
    // =========================================

    if (
        data.result &&
        data.result.insights &&
        data.result.insights.length > 0
    ) {

        html += `
            <h3>AI Insights</h3>
        `;


        data.result.insights.forEach(function (insight) {

            // -----------------------------------------
            // Convert description into bullet points
            // -----------------------------------------

            let description = insight.description || "";

            let points = description
                .split(".")
                .map(function (point) {
                    return point.trim();
                })
                .filter(function (point) {
                    return point.length > 0;
                });


            html += `

                <div class="insight-card">

                    <h4>
                        ${insight.title}
                    </h4>

                    <ul class="key-points">
            `;


            // -----------------------------------------
            // Display each point as bullet
            // -----------------------------------------

            points.forEach(function (point) {

                html += `
                        <li>
                            ${point}.
                        </li>
                `;

            });


            html += `

                    </ul>

                </div>

            `;

        });

    }


// =========================================
// TREND PREDICTIONS
// =========================================

    if (
        data.result &&
        data.result.predictions &&
        data.result.predictions.length > 0
    ) {

        html += `
            <h3>Trend Predictions</h3>
        `;


        data.result.predictions.forEach(function (prediction) {

            html += `

                <div class="prediction-card">

                    <strong>
                        ${prediction.column}
                    </strong>

                    <span>
                        ${prediction.trend}
                    </span>

                </div>

            `;

        });

    }


// =========================================
// TABULAR DATA
// =========================================

    if (
        data.result &&
        data.result.type === "tabular"
    ) {

        html += `

            <div class="file-info">

                <p>
                    <strong>Total Rows:</strong>
                    ${data.result.rows}
                </p>

                <p>
                    <strong>Columns:</strong>
                    ${data.result.columns.join(", ")}
                </p>

            </div>

        `;

    }


// =========================================
// PDF DATA
// =========================================

    if (
        data.result &&
        data.result.type === "pdf"
    ) {

        html += `

            <div class="file-info">

                <p>
                    <strong>Document Type:</strong>
                    PDF
                </p>

                <p>
                    <strong>Text Length:</strong>
                    ${data.result.text_length}
                    characters
                </p>

            </div>

        `;

    }


// =========================================
// SHOW RESULT
// =========================================

    result.innerHTML = html;


    result.style.display = "block";
    result.style.visibility = "visible";
    result.style.opacity = "1";


    console.log("RESULT DISPLAYED");


    // DEBUG: Check result after 2 seconds
    setTimeout(function () {

        console.log(
            "RESULT AFTER 2 SECONDS:",
            result.innerHTML
        );


        console.log(
            "RESULT DISPLAY:",
            result.style.display
        );


        console.log(
            "RESULT VISIBILITY:",
            result.style.visibility
        );


        console.log(
            "RESULT OPACITY:",
            result.style.opacity
        );

    }, 2000);

}

