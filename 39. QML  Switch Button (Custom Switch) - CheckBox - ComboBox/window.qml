import QtQuick 2.5
import QtQuick.Controls 2.5

ApplicationWindow{

    visible: true
    title: "Persian Python"
    color:"lightgrey"
    height: 500
    width: 500


    Column{
    anchors.centerIn:parent
    spacing:50

    Switch{
    text:"WIFI"
    id:myswitch
    onClicked:{window.hello(myswitch.checked)}
    }

    CheckBox{
    text:"PersianPython"
    id:mycheckbox
    onClicked:{window.hello(mycheckbox.checked)}
    }
    ComboBox{
    id:mycombo
    model:["TEst1", "test2"]
    onActivated:{window.hello(mycombo.currentValue)}
    }

    }

}