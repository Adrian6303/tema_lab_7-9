from domain.entities import Student
from domain.entities import PbLaborator
from domain.validators import Validator
from repository.lab_repo import InMemoryRepository
from service.lab_service import LabService
from ui.console import Console

repo = InMemoryRepository()
val = Validator()
srv = LabService(repo, val)
ui = Console(srv)
ui.gestiune_lab_ui()
