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
    Label{
        id:mylabel
        text:"My Label"
        font.pixelSize:30
        font.italic:true
        font.bold:true
        }
    Button{
        id:mybutton
        text:"Click On Me"
        onPressed:{
            mylabel.text="Clicked !"
            window.hello(mybutton.pressed)
        }
        background: Rectangle{
        border.width: 1
        border.color:"red"
        radius:10
        color: mybutton.pressed ? "green" : "blue"
        }

        }
}
}