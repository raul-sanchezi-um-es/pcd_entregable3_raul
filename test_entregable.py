import pytest
from entregable1.entregable1 import Persona, Asignatura, Estudiante, ProfesorTitular, ProfesorAsociado, MiembroDpto, Investigador, Universidad
from entregable1.entregable1 import ErrorAsignatura, ErrorFormato, ErrorDepartamento, ErrorMiembro

def test_creacion_universidad():
    universidad = Universidad("Universidad de Prueba")
    assert universidad.nombre == "Universidad de Prueba"


def test_creacion_persona():
    persona = Persona('Raul','123A','calle 1', 'V')
    assert persona._dni == '123A'
    assert persona._nombre == 'Raul'
    assert persona._direccion == 'calle 1'
    assert persona._sexo == 'V'



def test_creacion_asignatura():
    asignatura = Asignatura("Matemáticas", 6)
    assert asignatura.name == "Matemáticas" #Comprobamos que el nombre de la asignatura creada sea Matemáticas
    assert asignatura.creditos == 6 #Comprobamos que los creditos sean 6

def test_estudiante_matricularse():
    estudiante = Estudiante('Raul','123A','calle 1', 'V', [])
    matematicas = Asignatura("Matemáticas", 6)
    estudiante.añadir_asignatura(matematicas) #Lo matriculamos en matemáticas
    assert matematicas in estudiante.asignaturas_matriculadas #Comprobamos que matemáticas se haya metido en estudiante

def test_estudiante_eliminar_asignatura():
    fisica = Asignatura("Física", 6)
    estudiante = Estudiante("Maria", "022H", "Calle 4", "M", [fisica]) # Metemos que Maria estudia física
    estudiante.elimina_asignatura(fisica) # Eliminamos física 
    assert fisica not in estudiante.asignaturas_matriculadas # Comprobamos que física ya no está 

def test_error_estudiante_asignaturas():
    with pytest.raises(ErrorAsignatura):
        Estudiante("Carlos", "778K", "Calle 5", "V", "Fisica")  # Comprobamos que salta error

def test_creacion_miembro_departamento():
    miembro = MiembroDpto("Clara", "555U", "Calle 6", "M", "DIIC") # Creamos un miembro de departamento 
    assert miembro._nombre == "Clara"
    assert miembro._direccion == "Calle 6"
    assert miembro._departamento == "DIIC"


def test_profesor_titular_investigacion():
    profesor = ProfesorTitular("Jose", "212P", "Calle 44", "V", "DIIC", "Programación", [])
    assert profesor._area_investigacion == "Programación"
    assert profesor.obtener_departamento() == "DIIC"

def test_miembro_cambiar_departamento():
    miembro = MiembroDpto("Javier", "567F", "Calle 7", "V", "DITEC")
    miembro.cambiar_departamento("DIS")
    assert miembro.obtener_departamento() == "DIS" # Comprobamos que se ha cambiado el departamento

def test_eliminar_asignatura():
    fisica = Asignatura("Física", 4)
    profesor = ProfesorTitular("Javiera", "212C", "Calle 22", "M", "DITEC", "Departamento1", [fisica])
    profesor.elimina_asignatura(fisica)
    assert fisica not in profesor.asignaturas_impartidas

def test_añadir_asignatura():
    fisica = Asignatura("Física", 4)
    profesor = ProfesorTitular("Javiera", "212C", "Calle 22", "M", "DITEC", "Departamento1", [])
    profesor.añadir_asignatura(fisica)
    assert fisica in profesor.asignaturas_impartidas

