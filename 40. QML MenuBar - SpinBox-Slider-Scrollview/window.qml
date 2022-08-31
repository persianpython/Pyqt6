import QtQuick 2.5
import QtQuick.Controls 2.5

ApplicationWindow{
    visible: true
    title: "Persian Python"
    color:"lightgrey"
    height: 500
    width: 500

    menuBar:MenuBar{
    Menu{title:"File"
    Action{text:"New"}
    Action{text:"Open"}
    }
    }

    ScrollView{
    width: 200
    height: 200
    Label{
    id:mylabel
    text:"qweqweqw"
    font.pixelSize: 500
    }

    }

    Column{
    anchors.centerIn:parent
    spacing:50



    }

}