const { app, BrowserWindow } = require('electron');

function ElectronMainMethod() {
    const launchWindow = new BrowserWindow({
        title: 'LaughLoud',
        icon: 'static/img/favicon.ico',
        show: false // Fenster zunächst nicht anzeigen
    });

    const appURL = 'http://localhost:8000';
    launchWindow.loadURL(appURL);

    // Zeige das Fenster, sobald die Seite geladen ist
    launchWindow.webContents.on('did-finish-load', () => {
        launchWindow.show();
        launchWindow.maximize();
    });
}

app.whenReady().then(ElectronMainMethod);
