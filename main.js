// window.onload = function () {
//     chrome.tabs.query({ currentWindow: true, active: true }, function (tabs) {
//         chrome.tabs.sendMessage(tabs[0].id, { message: "popup_open" });
//     });
// }

document.querySelector(".scan").addEventListener("click", function () {
    // chrome.tabs.query({ currentWindow: true, active: true }, function (tabs) {
    //     chrome.tabs.sendMessage(tabs[0].id, { message: "analyze_site" });
    // });
    var data = 1;//this data will be the result coming from trained model
    if (data === 1) {
        document.querySelector(".IfDetected").style.display = 'block';

    }
    else {
        document.querySelector(".IfNotDetected").style.display = 'block';

    }
})

