class ErrorFormato(Exception):
    """Excepción por errores con el formato"""
    pass

class ErrorAsignatura(Exception):
    """Excepción por errores con las asignaturas"""
    pass

class ErrorDepartamento(Exception):
    """Excepción por errores con los departamentos"""
    pass

class ErrorMiembro(Exception):
    """Excepción por errores con los miembros"""
    pass


class Asignatura(): #Creamos esta clase para las asignaturas
    def __init__(self,name,creditos):
        self.name = name
        self.creditos = creditos
    def __eq__(self, other):
        if isinstance(other, Asignatura):
            return self.name == other.name and self.creditos == other.creditos
        return False

class Persona: #Creamos una clase persona de la que heredaran los demás sus atributos con los datos que nos piden
    def __init__(self, nombre, dni, direccion, sexo): #inicializamos la clase
        self._nombre = nombre
        self._dni = dni
        self._direccion = direccion
        if sexo not in ['V', 'M']:
            raise ErrorFormato('El sexo debe ser V o M')
        self._sexo = sexo

    def devuelve_datos(self):  #creamos esta función para que podamos mostrar los datos de la persona ya que son privados
        return 'Nombre: '+ self._nombre + ' DNI: '+ self._dni + ' Dirección: '+ self._direccion+' Sexo : '+self._sexo

class MiembroDpto(Persona): #Creamos la clase miembrodpto que hereda de persona y además tiene los atributos departamento y el tipo de miembro que es
    def __init__(self, nombre, dni, direccion, sexo, departamento): #inicializamos el miembro dpto
        super().__init__(nombre,dni,direccion,sexo) #inicializamos la clase que heredamos de persona
        if departamento not in ['DIIC','DITEC','DIS']:
            raise ErrorDepartamento('El departamento debe ser DIIC, DITEC, DIS')
        self._departamento = departamento

    def obtener_departamento(self):
        return self._departamento
    
    def cambiar_departamento(self, nuevo_depto): #Creamos esta función para que se pueda cambiar de dpto
        if nuevo_depto not in ['DIIC','DITEC','DIS']:
            raise ErrorDepartamento('El departamento debe ser DIIC, DITEC, DIS')
        self._departamento = nuevo_depto

    def devuelve_datos(self): #creamos esta función para que podamos mostrar los datos del miembro dpto ya que son privados
        return 'Nombre: '+ self._nombre + ' DNI: '+ self._dni + ' Dirección: '+ self._direccion+' Sexo : '+self._sexo+' Departamento: '+self._departamento

class ProfesorAsociado(MiembroDpto): #Creamos la clase profesor asociado que hereda de miembro dpto
    def __init__(self, nombre, dni, direccion, sexo, departamento,asignaturas): #inicializamos el profesor asociado
        super().__init__(nombre, dni, direccion, sexo, departamento) #inicializamos la clase que heredamos de miembro dpto
        if type(asignaturas) is not list:
            raise ErrorFormato('Las asignaturas impartidas deben tener formato lista')
        
        for asignatura in asignaturas:
            if not isinstance(asignatura, Asignatura):
                raise ErrorFormato('Las asignaturas deben ser de la clase Asignatura')
        self.asignaturas_impartidas = asignaturas

    def devuelve_datos(self):#creamos esta función para que podamos mostrar los datos del profesor ya que son privados
        return 'Nombre: '+ self._nombre + ' DNI: '+ self._dni + ' Dirección: '+ self._direccion+' Sexo : '+self._sexo+' Departamento: '+self._departamento


    def obtener_asignaturas(self):
        return self.asignaturas_impartidas
    

    def añadir_asignatura(self,asignatura): #Creamos esta funcion para añadirle asignaturas que imparte
        if not isinstance(asignatura, Asignatura):
                raise ErrorFormato('Las asignaturas deben ser de la clase Asignatura')
        for a in self.asignaturas_impartidas:
            if(a == asignatura):
                raise ErrorAsignatura('Previamente imparte esa asignatura') #si vemos que la asignatura ya está en el array que tiene de impartidas hacemos excepcion

        self.asignaturas_impartidas.append(asignatura) #si no coincide, la añadimos

    def elimina_asignatura(self,asignatura):#Creamos esta función para retirar una asignatura que da
        if not isinstance(asignatura, Asignatura):
                raise ErrorFormato('Las asignaturas deben ser de la clase Asignatura')
        for a in self.asignaturas_impartidas:
            if(a == asignatura):
                self.asignaturas_impartidas.remove(asignatura) 
                return
        raise ErrorAsignatura('No imparte esa asignatura') #si no encuentra la asignatura entre las que imparte, hacemos excepción


class Investigador(MiembroDpto): #Creamos la clase investigador que hereda de miembro dpto
    def __init__(self, nombre, dni, direccion, sexo, departamento, area_investigacion):#inicializamos el investigador
        super().__init__(nombre, dni, direccion, sexo, departamento)#inicializamos la clase que heredamos de miembro dpto
        self._area_investigacion = area_investigacion

    def devuelve_datos(self):#creamos esta función para que podamos mostrar los datos del investigador ya que son privados
        return 'Nombre: '+ self._nombre + ' DNI: '+ self._dni + ' Dirección: '+ self._direccion+' Sexo : '+self._sexo+' Departamento: '+self._departamento+' Area investigacion: '+self._area_investigacion


class ProfesorTitular(Investigador):#Creamos la clase profesor titular que hereda de miembro dpto
    def __init__(self, nombre, dni, direccion, sexo, departamento, area_investigacion,asignaturas):#inicializamos el profesor titular
        super().__init__(nombre, dni, direccion, sexo, departamento, area_investigacion)#inicializamos la clase que heredamos de investigador
        if type(asignaturas) is not list:
            raise ErrorFormato('Las asignaturas impartidas deben tener formato lista')
        
        for asignatura in asignaturas:
            if not isinstance(asignatura, Asignatura):
                raise ErrorFormato('Las asignaturas deben ser de la clase Asignatura')
        self.asignaturas_impartidas = asignaturas

    def devuelve_datos(self):#creamos esta función para que podamos mostrar los datos del profesor ya que son privados
            return 'Nombre: '+ self._nombre + ' DNI: '+ self._dni + ' Dirección: '+ self._direccion+' Sexo : '+self._sexo+' Departamento: '+self._departamento+' Area investigacion: '+self._area_investigacion

    def añadir_asignatura(self,asignatura): #Creamos esta funcion para añadirle asignaturas que imparte
        if not isinstance(asignatura, Asignatura):
                raise ErrorFormato('Las asignaturas deben ser de la clase Asignatura')
        for a in self.asignaturas_impartidas:
            if(a == asignatura):
                raise ErrorAsignatura('Previamente imparte esa asignatura') #si vemos que la asignatura ya está en el array que tiene de impartidas hacemos excepcion

        self.asignaturas_impartidas.append(asignatura) #si no coincide, la añadimos

    def elimina_asignatura(self,asignatura):#Creamos esta función para retirar una asignatura que da
        if not isinstance(asignatura, Asignatura):
                raise ErrorFormato('Las asignaturas deben ser de la clase Asignatura')
        for a in self.asignaturas_impartidas:
            if(a == asignatura):
                self.asignaturas_impartidas.remove(asignatura) 
                return
        raise ErrorAsignatura('No imparte esa asignatura') #si no encuentra la asignatura entre las que imparte, hacemos excepción


class Estudiante(Persona):#Creamos la clase profesor titular que hereda de persona
    def __init__(self, nombre, dni, direccion, sexo, asignaturas): #inicializamos el estudiante
        super().__init__(nombre, dni, direccion, sexo) #inicializamos la persona de la que hereda
        if type(asignaturas) is not list:
            raise ErrorFormato('Las asignaturas impartidas deben tener formato lista')
        for asignatura in asignaturas:
            if not isinstance(asignatura, Asignatura):
                raise ErrorFormato('Las asignaturas deben ser de la clase Asignatura')
        self.asignaturas_matriculadas = asignaturas

    def devuelve_datos(self): #creamos esta función para que podamos mostrar los datos del estudiante ya que son privados
        return 'Nombre: '+ self._nombre + 'DNI: '+ self._dni + 'Dirección: '+ self._direccion+'Sexo : '+self._sexo

    def añadir_asignatura(self,asignatura):  #Creamos esta clase para añadirle asignaturas 
        if not isinstance(asignatura, Asignatura):
                raise ErrorFormato('Las asignaturas deben ser de la clase Asignatura')
        for a in self.asignaturas_matriculadas: 
            if(a == asignatura):
                raise ErrorAsignatura('Previamente matriculado en esa asignatura') #si vemos que coincide con alguna asignatura que ya da, hacemos excepcion
                
        self.asignaturas_matriculadas.append(asignatura) # si no, la añadimos

    def elimina_asignatura(self,asignatura): #creamos esta clase para eliminarle asignaturas
        if not isinstance(asignatura, Asignatura):
                raise ErrorFormato('Las asignaturas deben ser de la clase Asignatura')
        for a in self.asignaturas_matriculadas:
            if(a == asignatura):
                self.asignaturas_matriculadas.remove(asignatura) 
                return
        raise ErrorAsignatura('No matriculado en esa asignatura') # si vemos que no coincide, es que no la la está dando


class Universidad: #creamos la clase universidad de donde sale todo
    def __init__(self,nombre): #inicializamos con el nombre y todas las listas vacías
        self.nombre = nombre
        self._miembros_departamento = []
        self._estudiantes = []
        self._profesores_titulares = []
        self._profesores_asociados = []
        self._investigadores = []


    def agregar_miembro_departamento(self, nombre, dni, direccion, sexo, departamento): #Creamos esta función para agregar un nuevo miembro de dpto
        for a in self._miembros_departamento:
            if(a._dni == dni):
                raise ErrorMiembro('Ya está en la universidad') #Si ya está este miembro, hay excepcion
        self._miembros_departamento.append(MiembroDpto(nombre, dni, direccion, sexo,departamento)) # lo añadimos

    def eliminar_miembro_departamento(self, dni): #Creamos esta función para eliminar un miembro de dpto
        for a in self._miembros_departamento:
            if(a._dni == dni):
                self._miembros_departamento.remove(a) #lo quitamos
                return
        raise ErrorMiembro('No está en la universidad') #si no está, hay excepción
    

 
    def agregar_profesor_asociado(self, nombre, dni, direccion, sexo, departamento,asignaturas): #Creamos esta función para agregar un nuevo profesor
        for a in self._profesores_asociados:
            if(a._dni == dni): 
                raise ErrorMiembro('Ya está en la universidad') #Si el dni coincide con otro que ya esté, ya está y hay excepción
        self._profesores_asociados.append(ProfesorAsociado(nombre, dni, direccion, sexo,departamento,asignaturas)) #lo añadimos
        self.agregar_miembro_departamento(nombre, dni, direccion, sexo, departamento) #si hay un profesor también es miembro de departamento, por lo que lo añadimos

    def eliminar_profesor_asociado(self, dni):  #Creamos esta función para eliminar un profesor
        for a in self._profesores_asociados:
            if(a._dni == dni):
                self._profesores_asociados.remove(a)#Si el dni coincide con otro que ya esté, lo quitamos
                self.eliminar_miembro_departamento(a) #quitamos también el miembro de dpto
                return
        raise ErrorMiembro('No está en la universidad') #Si el dni no coincide con otro que ya esté, no existe el profesor y hay excepción


    def agregar_profesor_titular(self, nombre, dni, direccion, sexo, departamento, area_investigacion,asignaturas): #Creamos esta función para agregar un nuevo profesor
        for a in self._profesores_titulares:
            if(a._dni == dni):
                raise ErrorMiembro('Ya está en la universidad') #Si el dni coincide con otro que ya esté, ya está y hay excepción
        self._profesores_titulares.append(ProfesorTitular(nombre, dni, direccion, sexo, departamento, area_investigacion,asignaturas))  #lo añadimos
        self.agregar_investigador(nombre, dni, direccion, sexo, departamento,area_investigacion) #si hay un profesor también es investigador, por lo que lo añadimos

    def eliminar_profesor_titular(self, dni):  #Creamos esta función para eliminar un profesor
        for a in self._profesores_titulares:
            if(a._dni == dni):
                self._profesores_titulares.remove(a) #Si el dni coincide con otro que ya esté, lo quitamos
                self.eliminar_investigador(a) #quitamos también el investigador
                return
        raise ErrorMiembro('No está en la universidad') #Si el dni no coincide con otro que ya esté, no existe el profesor y hay excepción
    

    def agregar_investigador(self, nombre, dni, direccion, sexo, departamento, area_investigacion): #Creamos esta función para agregar a un nuevo investigador
        for a in self._investigadores:
            if(a._dni == dni):
                raise ErrorMiembro('Ya está en la universidad') #Si el dni coincide con otro que ya esté, ya está y hay excepción
        self._investigadores.append(Investigador(nombre, dni, direccion, sexo, departamento, area_investigacion)) #lo añadimos
        self.agregar_miembro_departamento(nombre, dni, direccion, sexo, departamento,) #si hay un investigador también es miembro de departamento, por lo que lo añadimos

    def eliminar_investigador(self, dni): #Creamos esta funciíon para eliminar un investigador
        for a in self._investigadores:
            if(a._dni == dni):
                self._investigadores.remove(a) #lo quitamos
                self.eliminar_miembro_departamento(a) #quitamos también al miembro de dpto que es
                return
        raise ErrorMiembro('No está en la universidad') #Si el dni no coincide con otro que ya esté, no existe el profesor y hay excepción

    def cambiar_departamento_miembro(self, miembro, nuevo_depto): #hacemos esta función para que un miembro de dpto cambio de dpto
        for a in self._miembros_departamento:
            if(a._dni == miembro):
                a.cambiar_departamento(nuevo_depto)

    def agregar_estudiante(self, nombre, dni, direccion, sexo,asignaturas): #Creamos esta función para agregar a un nuevo estudiante
        for a in self._estudiantes:
            if(a._dni == dni):
                raise ErrorMiembro('Ya está matriculado en la universidad') #si el dni coincide, ya está y tenemos excepción
        self._estudiantes.append(Estudiante(nombre, dni, direccion, sexo,asignaturas)) #lo añadimos si no está

    def eliminar_estudiante(self, dni): #Creamos esta función para eliminar un estudiante
        for a in self._estudiantes:
            if(a._dni == dni):
                self._estudiantes.remove(a) #lo quitamos
                return
        raise ErrorMiembro('No matriculado en la universidad') #si no está entre los estudiantes, tenemos excepción
    
    def listado_miembros(self): #Creamos esta función para listar todos los miembros de dpto que tenemos
        for a in self._miembros_departamento:
            print(a.devuelve_datos())



if __name__ == "__main__":

    # Crear asignaturas
    asignatura1 = Asignatura("Matemáticas", 6)
    asignatura2 = Asignatura("Física", 4)
    asignatura3 = Asignatura("Química", 5)
    asignatura4 = Asignatura("Programación", 6)

    # Crear universidad
    universidad = Universidad("Universidad Ejemplo")

    # Agregar estudiantes
    universidad.agregar_estudiante("Juan Pérez", "12345678A", "Calle Falsa 123", "V", [asignatura1, asignatura2])
    universidad.agregar_estudiante("Ana Gómez", "87654321B", "Avenida Siempre Viva 456", "M", [asignatura3, asignatura4])

    # Agregar profesores asociados
    universidad.agregar_profesor_asociado("Luis Fernández", "11223344C", "Calle de la Luna 7", "V", "DIIC",[asignatura1])
    universidad.agregar_profesor_asociado("María López", "44332211D", "Calle del Sol 8", "M", "DITEC",[asignatura2])

    # Agregar profesores titulares
    universidad.agregar_profesor_titular("Carlos García", "55667788E", "Plaza Mayor 9", "V", "DIS", "Inteligencia Artificial",[asignatura3])
    universidad.agregar_profesor_titular("Elena Ruiz", "99887766F", "Avenida del Mar 10", "M", "DIIC", "Redes de Computadores",[asignatura4])

    # Agregar investigadores
    universidad.agregar_investigador("Miguel Sánchez", "33445566G", "Calle de las Flores 11", "V", "DIIC", "Machine Learning")
    universidad.agregar_investigador("Lucía Díaz", "66554433H", "Calle del Río 12", "M", "DIS", "Ciberseguridad")

    # Mostrar datos de los miembros del departamento
    print("Miembros del departamento:")
    universidad.listado_miembros()

        # Añadir asignaturas a un profesor asociado
    profesor_asociado = universidad._profesores_asociados[0]  # Luis Fernández
    profesor_asociado.añadir_asignatura(asignatura3)
    profesor_asociado.añadir_asignatura(asignatura4)

    # Eliminar una asignatura de un estudiante
    estudiante = universidad._estudiantes[0]  # Juan Pérez
    estudiante.elimina_asignatura(asignatura1)

    # Cambiar departamento de un miembro
    universidad.cambiar_departamento_miembro(profesor_asociado._dni, "DIS")

    # Mostrar datos actualizados de los miembros del departamento
    print("\nMiembros del departamento:")
    universidad.listado_miembros()






    

