const {app, BrowserWindow} = require('electron')

function ElectronMainMethod() {
    const launchWindow = new BrowserWindow({
        title: 'LaughLoud',
        icon: 'static/img/favicon.ico'
    })

    const appURL = 'http://localhost:8000';
    launchWindow.loadURL(appURL);
} // end main()

app.whenReady().then(ElectronMainMethod)