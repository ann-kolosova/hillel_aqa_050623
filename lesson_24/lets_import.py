
from pathlib import Path
import sys
# filepath to Path obj
print(sys.path)
print("*"*8)
p = Path(__file__)
print(p) # шлях до файлу
print(p.parent) # шлях до папки де він лежить
print(p.parent.parent) # шлях до батьківської папки де він лежить
p_logger = p.parent.parent / "lesson_23"
sys.path.insert(0, str(p.parent.parent))
sys.path.insert(0, str(p_logger))
import compare_code_speed
from logger import logger
compare_code_speed.func_a([1,2,3])
logger.info("my log")
print("*"*8)
print(sys.path)


