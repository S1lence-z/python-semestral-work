# main_controller.py
from models.database_manager import DatabaseManager
from controllers.view_controller import ViewController
from controllers.home_controller import HomeController
from controllers.editation_controller import EditationController
from controllers.addition_controller import AdditionController
from controllers.page_controller_abc import PageController

class MainController:
    def __init__(self, model: DatabaseManager, view: ViewController) -> None:
        self.model = model
        self.view = view
        self.page_controllers = self._init_page_controllers()
    
    def _init_page_controllers(self) -> list[PageController]:
        """ Initialize all controllers.

        Returns:
            list: A list of all controllers.
        """
        home_controller = HomeController(self.model, self.view)
        editation_controller = EditationController(self.model, self.view)
        addition_controller = AdditionController(self.model, self.view)
        return [home_controller, editation_controller, addition_controller]
    
    def start_app(self):
        self.view.raise_page("home")
        self.view.start_mainloop()