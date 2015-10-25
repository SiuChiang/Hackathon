from javafx.application import Application
from javafx.scene import Scene
from javafx.scene.control import Label
from javafx.scene.layout import AnchorPane

class frame(Application):
    def start(self,stage):
        stage.setTitle("Hello, World!")

        root = AnchorPane()
        label = Label("Hello, World!")
        root.getChildren().add(label)

        scene = Scene(root, 100, 40)
        stage.setScene(scene)

        stage.show()

if __name__ == '__main__':
    Application.launch(Hello().class, [])
