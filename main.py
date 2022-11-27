from domain.entities import Student
from domain.entities import PbLaborator
from domain.validators import Validator
from repository.lab_repo import InMemoryRepository
from service.lab_service import LabService
from service.lab_service import StudentService
from service.lab_service import GradeService
from ui.console import Console
from service.generate_values import Random

repo = InMemoryRepository()
val = Validator()
student_repo = InMemoryRepository()
pbLab_repo = InMemoryRepository()
srvL = LabService(repo, val)
srvS = StudentService(repo, val)
srvR = Random(repo, val)
srvG = GradeService(repo, val)
ui = Console(srvL, srvS, srvR, srvG)
ui.gestiune_lab_ui()
