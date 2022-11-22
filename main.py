from domain.entities import Student
from domain.entities import PbLaborator
from domain.validators import Validator
from repository.lab_repo import InMemoryRepository
from service.lab_service import LabService
from service.lab_service import StudentService
from ui.console import Console
from service.generate_values import Random

repo = InMemoryRepository()
val = Validator()
srvL = LabService(repo, val)
srvS = StudentService(repo, val)
srvR = Random(repo, val)
ui = Console(srvL,srvS,srvR)
ui.gestiune_lab_ui()
