from domain.entities import Student
from domain.entities import PbLaborator
from domain.validators import Validator
from repository.lab_repo import InMemoryRepository
from service.lab_service import LabService
from service.lab_service import StudentService
from ui.console import Console

repo = InMemoryRepository()
val = Validator()
srvL = LabService(repo, val)
srvS = StudentService(repo, val)
ui = Console(srvL,srvS)
ui.gestiune_lab_ui()
