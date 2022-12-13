document
    .querySelector("#enterButton")
    .addEventListener("keypress", function (e) {
        if (e.key === "Enter") {
            document.enterButtonName.submit();
        }
    });
