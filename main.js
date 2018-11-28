const electron = require("electron");
const url = require('url');
const path = require('path');

const { app, BrowserWindow, Menu } = electron;

let mainWindow;

//listen for app to be ready
app.on('ready', function (){
    mainWindow = new BrowserWindow({});
    //Load html into the window
    mainWindow.loadURL(url.format({
       pathname: path.join(__dirname, 'mainWindow.html'),
       protocol: "file:",
       slashes: true
    }));

    //Quit App when closed
      mainWindow.on('closed', function (){
        app.quit();
    });

    // Build menu from Template
    const mainMenu = Menu.buildFromTemplate(mainMenuTemplate);
    //Insert menu
    Menu.setApplicationMenu(mainMenu);

});

//Create menu Template
const mainMenuTemplate = [
    {},
    {
        label: 'File',
        submenu: [
            {
                label: 'Run new task',
               // click
            },
            {
                label: 'Quit',
                accelerator: process.platform == 'darwin' ?'Command+Q' : 'Ctrl+Q',
                click(){
                    app.quit();
                }
            }
        ]
    },
    {
        label: 'Options'
    }
];

//Add developer tools item if not in production
if (process.env.NODE_ENV !== 'production') {
    mainMenuTemplate.push({
        label: 'View',
        submenu: [
            {
                label: 'Developer Tools',
                submenu: [
                    {
                        label: 'Toogle DevTools',
                        aaccelerator: process.platform == 'darwin' ? 'Command+I' : 'Ctrl+I',
                        click(item, focusedWindow) {
                            focusedWindow.toggleDevTools();
                        }
                    }]
            },
            {
                role: 'reload'
            }]
    });
}