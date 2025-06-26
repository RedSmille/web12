from datetime import datetime
import random

# Obtiene la respuesta basada en la intención detectada
def ObtenerRespuesta(ListaIntentos, JsonIntentos):

    def generar_respuesta_area(nombre_area, emoji, piso, encargado, extensiones):

        pisos = {
            "0": "Planta Baja",
            "1": "Piso 1",
            "2": "Piso 2",
            "3": "Piso 3",
            "4": "Piso 4",
            "5": "Piso 5",
            "6": "Piso 6",
            "7": "Edificio Viejo",	
        }

        piso = pisos.get(piso, piso)
        
        card = (
            f'<section class="card">'
                f'<header>'
                    f'<p><b>{nombre_area} <span class="emoji3">{emoji}</span></b> <b><button class="info pisos" onclick="Mostrar(\'{piso}\')">{piso}</button></b> </p>'
                    f'<p>{encargado}</p>'
                f'</header>'
            f'</section>'
        )
        
        botones_ext = ""
        for descripcion, ext in extensiones:
            botones_ext += f'<b> </b><a href="tel:6677126606,{ext}"><button class="archivo"><b>{descripcion}: </b>{ext}</button></a>'
        
        return [card, Respuesta, TelefonoPrincipal + botones_ext]

    if not ListaIntentos or ListaIntentos[0]['Intencion'] == 'unknown':
        return [
            "Lo siento, no tengo información sobre ese tema. <b>¿Puedes preguntar algo más relacionado con el hospital?</b>",
            '<b>También puedes utilizar</b> los botones de arriba ⬆️ para explorar las áreas y los tópicos de atención.'
        ]
    
    Ayuda = "<b>¿En qué más te puedo ayudar?</b> Pregúntame lo que necesites o utiliza los botones de arriba ⬆️ para explorar las <b>Áreas</b> y los <b>Tópicos</b> de atención."
    InfoContacto = '<b>Correo: </b> <a href="mailto:alianzaestrategica@hps.org.mx"><button class="info" style="margin-bottom: 5px; margin-top: 0px;" >alianzaestrategica@hps.org.mx ✉️</button></a>\n<b>Teléfono Principal y Extensiones:\n</b> <a href="tel:6677126606"><button class="info">6677126606 📞</button></a><b> </b><a href="EXTENSIONES.pdf" target="_blank"><button class="archivo">Todas las Extensiones ➡️</button></a>'
    TelefonoPrincipal = '<b>Teléfono Principal y Extensión</b> \n<a href="tel:6677126606"><button class="info">6677126606 📞</button></a>'

    Etiqueta = ListaIntentos[0]['Intencion']    
    
    for Intento in JsonIntentos['intents']:
        if Intento['tag'] == Etiqueta:
            # Se elige una respuesta aleatoria
            Respuesta = random.choice(Intento['respuestas'])

            # Comparar directamente con el tag en lugar de la respuesta
            if Intento['tag'] == "fecha":
                FechaActual = datetime.now().strftime("%A, %d de %B del %Y")
                return [f"Hoy es {FechaActual}", Ayuda]
            
            elif Intento['tag'] in ["saludo", "saludo_2"]:
                return [
                    Respuesta,
                    Ayuda
                ]
            elif Intento['tag'] == "hora":
                HoraActual = datetime.now().strftime("%H:%M")
                return [f"Son las {HoraActual}", Ayuda]
            elif Intento['tag'] == "logo":
                return [
                    Respuesta,
                    Ayuda
                ] 
            elif Intento['tag'] == "informacion_general":
                return [
                    Respuesta,
                    InfoContacto
                ]
            elif Intento['tag'] == "informacion_adicional":
                return [
                    Respuesta,
                    InfoContacto
                ]

            elif Intento['tag'] == "historia_hospital":
                return [
                    Respuesta,
                    'Desde entonces, ha ampliado sus servicios médicos y actualmente ofrece casi todas las subespecialidades pediátricas. En 1993 fue reconocido como sede de posgrado en pediatría por la UAS, y en 1999 inició la subespecialidad en oncología pediátrica.',
                    '<img decoding="async" width="200" class="elemento_interno" src="MN.png" alt="">',
                    '<b>También puedes consultar</b>'
                    '\n<button class="info" onclick="Mostrar(\'Misión y Visión \')">Misión y Visión</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Valores\')">Valores</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Aniversario\')">Aniversario</button><b> </b>'
                ]
            elif Intento['tag'] == "ubicacion":
                return [
                    Respuesta,
                    '<iframe class="elemento_interno" src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3621.9029951692764!2d-107.40199942463111!3d24.79877497796962!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x86bcd0b34e811d65%3A0x7728b9f1122455ed!2sHospital%20Pedi%C3%A1trico%20de%20Sinaloa!5e0!3m2!1ses!2smx!4v1743604900818!5m2!1ses!2smx" width="300" height="200" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>',
                    Ayuda
                ]
            elif Intento['tag'] == "especialidades":
                return [
                    Respuesta,
                    f'<section class="card">'
                        f'<header>'
                            f'<p><b><span class="emoji3">🥼</span> <span class="emoji3">💉</span> <span class="emoji3">🩸</span></b> <b><button class="info pisos" onclick="Mostrar(\'Piso 2\')">Piso 2</button></b> </p>'
                            f'<p>Dr. Jorge Rolando Romero Bazua \nEnf. Shery Guadalupe Avendaño Morachis</p>'
                        f'</header>'
                    f'</section>',
                    f'<b>Todas las Especialidades disponibles</b>'
                    f'<div style="display: flex; gap: 20px;">'
                        f'<section class="card">'
                            f'<header>'
                                '<p>• Alergología\n• Cardiología\n• Cirugía Cardiovascular\n• Cirugía General'
                                '\n• Cirugía Plástica\n• Clínica de Obesidad\n• Comunicación Humana\n• Consulta de Urgencias'
                                '\n• Consulta Externa\n• Hematología\n• Endocrinología\n• Estomatología'
                                '\n• Foniatría y Audiología\n• Gastroenterología\n• Genética\n• Hematología</p>'
                            f'</header>'
                        f'</section>'
                        f'<section class="card">'
                            f'<header>'
                                '<p>• Infectología\n• Medicina Física y Rehabilitación\n• Medicina Interna\n• Nefrología'
                                '\n• Neonatología\n• Neumología\n• Neurología\n• Neurocirugía'
                                '\n• Nutrición\n• Oftalmología\n• Oncología\n• Ortodoncia'
                                '\n• Otorrinolaringología\n• Psicología\n• Traumatología y Ortopedia\n• Urología</p>'
                            f'</header>'
                        f'</section>'
                    '</div>',
                    '<b>Teléfono Principal y Extensiónes</b>'
                    '\n<a href="tel:6677126606"><button class="info">6677126606 📞</button></a>'
                    '<b> </b><a href="tel:6677126606,7038"><button class="archivo"><b>Especialidades: </b>7038</button></a>'
                    '<b> </b><a href="tel:6677126606,7039"><button class="archivo"><b>Especialidades Enfermeria: </b>7039</button></a>'
                    '<b> </b><a href="tel:6677126606,7107"><button class="archivo"><b>Jefatura Especialidades: </b>7107</button></a>'
                ]
            elif Intento['tag'] == "aniversario":
                return [
                    Respuesta,
                    '<img decoding="async" width="200" class="elemento_interno" src="F5.jpg" alt="">',
                    '<b>También puedes consultar</b>'
                    '\n<button class="info" onclick="Mostrar(\'Misión y Visión\')">Misión y Visión</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Valores\')">Valores</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Historia\')">Historia</button><b> </b>'
                ]
            elif Intento['tag'] == "pagina_web":
                return [
                    Respuesta,
                    '<button class="info" onclick="window.open(\'https://hospitalpediatrico.org/oficial/\', \'_blank\');">Pagina Web Oficial ➡️➡️🌐</button>'
                ]
            elif Intento['tag'] == "info_chatbot":
                return [
                    Respuesta,
                    "Estoy aquí para responder tus preguntas relacionadas con el hospital."
                ]
            elif Intento['tag'] == "telefono":
                return [
                    '<b>Teléfono Principal y Extensiones</b>'
                    '\n<a href="tel:6677126606"><button class="info" style="margin-bottom: 5px;">667 712 66 06 📞</button></a>'
                    '<b> </b><a href="EXTENSIONES.pdf" target="_blank"><button class="archivo" style="margin-bottom: 5px;">Todas las Extensiones ➡️</button></a>'+
                    Respuesta,
                    'También puedes preguntar por el área que deseas contactar y te proporcionaremos la <b>extensión específica.</b>',
                    '<b>Otros Teléfonos</b>'
                    '\n<a href="tel:6677139004"><button class="info">667 713 90 04 📞</button></a>'
                    '<b> </b><a href="tel:6677126607"><button class="info">667 712 66 07 📞</button></a>'
                    '\n<a href="tel:6677126608"><button class="info">667 712 66 08 📞</button></a>'
                    '<b> </b><a href="tel:6677133523"><button class="info">667 713 35 23 📞</button></a>'
                    '\n<a href="tel:6672612200"><button class="info">667 261 22 00 📞</button></a>'
                ]
            elif Intento['tag'] == "correo":
                return [
                    '<img decoding="async" width="150" class="elemento_interno" src="Gmail.gif" alt="">',
                    Respuesta,
                    'Brindamos atención oportuna y seguimiento a tus necesidades.',
                    '<b>Correo Electronico</b>'
                    '\n<a href="mailto:alianzaestrategica@hps.org.mx"><button class="info">alianzaestrategica@hps.org.mx ✉️</button></a>'
                ]
            elif Intento['tag'] == "consultas":
                return [
                    Respuesta,
                    'Visita la sección <b>Especializada</b> de la página del hospital. Ahí encontraras más requisitos específicos.'
                    '\n<button class="info" onclick="window.open(\'https://hospitalpediatrico.org/oficial/consulta/\', \'_blank\');">Información Consultas ➡️➡️🌐</button>',
                    TelefonoPrincipal + '<b> </b><a href="tel:6677126606,7038"><button class="archivo"><b>Citas: </b>7038</button></a>'
                    '<b> </b><a href="tel:6677126606,7039"><button class="archivo"><b>Citas Enfermería: </b>7039</button></a>'
                ]
            elif Intento['tag'] == "donaciones":
                return [
                    f'<section class="card">'
                        f'<header>'
                            f'<p><b>Donaciones <span class="info emoji">🎁</span> <span class="info emoji">🩸</span> <span class="info emoji">🪙</span></b></p>'
                        f'</header>'
                    f'</section>',
                    Respuesta,
                    '<b>Diferentes Tipos de Donaciones</b>'
                    '\n<button class="info" onclick="Mostrar(\'Donaciones de Sangre\')">Donaciones de Sangre</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Donaciones en Especie\')">Donaciones en Especie</button><b> </b>'
                ]
            elif Intento['tag'] == "donacion_sangre":
                return [
                    Respuesta,
                    f'<b>Requisitos Mínimos Para Donar Sangre</b>'
                    f'<div style="display: flex; gap: 20px;">'
                        f'<section class="card">'
                            f'<header>'
                                '<p>'
                                    '• Gozar De Buena Salud, Sentirse Bien.'
                                    '\n• Tener Entre 18 Y 65 Años De Edad.'
                                    '\n• Pesar Mínimo 50 Kg.'
                                    '\n• Ayuno De 4 Horas.'
                                    '\n• Identificación Oficial Vigente.'
                                    '\n• No Haber Ingerido Bebidas Alcohólicas 3 Dias Antes.'
                                    '\n• No Presentar Alguna Infección Aguda.'
                                    '\n• No Estar Embarazada Ni Lactando.'
                                    '\n• Ninguna Cirugía Mayor En Los Últimos 6 Meses.'
                                    '\n• No Haberse Realizado En Los Últimos 12 Meses Perforaciones, Tatuajes, Acupuntura Ni Piloelectrolisis.'
                                    '\n• No Haber Padecido Hepatitis A Después De Los 10 Años.'
                                '</p>'
                            f'</header>'
                        f'</section>'
                    f'</div>',
                    TelefonoPrincipal + '<b> </b><a href="tel:6677126606,7105"><button class="archivo"><b>Banco de Sangre TS: </b>7105</button></a>'
                    '<b> </b><a href="tel:6677126606,7065"><button class="archivo"><b>Oncología Banco de Sangre: </b>7065</button></a>'
                ]
            elif Intento['tag'] == "donacion_especie":
                return [
                    Respuesta,
                    f'<b>Áreas y tipo de bien relacionados</b>'
                    f'<div style="display: flex; gap: 20px;">'
                        f'<section class="card">'
                            f'<header>'
                                '<p>'
                                    '<button class="info" onclick="Mostrar(\'Informatica\')">Informatica</button> <span class="emoji3">➡️</span> \n • Equipo de Computo'
                                    '\n<button class="info" onclick="Mostrar(\'Mantenimiento\')">Mantenimiento</button> <span class="emoji3">➡️</span> \n • Mobiliario'
                                    '\n<button class="info" onclick="Mostrar(\'Subdirección Médica\')">Subdirección Médica</button> <span class="emoji3">➡️</span> \n • Reactivos y Medicamentos'
                                    '\n<button class="info" onclick="Mostrar(\'Biomédica\')">Biomédica</button> <span class="emoji3">➡️</span> \n • Equipo Médico'
                                    '\n<button class="info" onclick="Mostrar(\'Servicios Generales\')">Servicios Generales</button> <span class="emoji3">➡️</span> \n • Automóviles, Camillas, Sillas de Ruedas'
                                    '\n<button class="info" onclick="Mostrar(\'Subdirección Administrativa\')">Subdirección Administrativa</button> <span class="emoji3">➡️</span> \n • Cualquier otro activo'
                                '</p>'
                            f'</header>'
                        f'</section>'
                    f'</div>',
                    TelefonoPrincipal + '<b> </b><a href="tel:6677126606,7004"><button class="archivo"><b>Alianza Estratégica: </b>7004</button></a>'
                ]
            elif Intento['tag'] == "redes_sociales":
                return [
                    Respuesta,
                    '<b>Redes Sociales Oficiales:</b>'
                    '\n<button class="info" style="background-color:#1877f2;" onclick="window.open(\'https://www.facebook.com/profile.php?id=100083151401330\', \'_blank\');"><i class="fab fa-facebook"></i> Facebook</button> '
                    '<b> </b><button class="info" style="background: linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888);" onclick="window.open(\'https://www.instagram.com/hospitalpediatricodesinaloa?igsh=MTVvZmkxZ25obTMybw%3D%3D\', \'_blank\');"><i class="fab fa-instagram"></i> Instagram</button> '
                    '<b> </b><button class="info" style="background-color: black" onclick="window.open(\'https://x.com/pediatrico\', \'_blank\');"><i class="fab fa-twitter"></i> Twitter</button>'
                ]
            elif Intento['tag'] == "extensiones":
                return [
                    Respuesta +
                    '\n<a href="EXTENSIONES.pdf" target="_blank"><button class="archivo">Todas las Extensiones ➡️</button></a>',
                    'También puedes preguntar por el área que deseas contactar y te proporcionaremos la <b>extensión específica.</b>',
                    '<b>Teléfono Principal</b>'
                    '\n<a href="tel:6677126606"><button class="info">667 712 66 06 📞</button></a>'
                ]
            elif Intento['tag'] == "mision_vision":   
                return [
                    Respuesta,
                    '<b>Vision:</b> Ser un hospital líder a nivel nacional en atención pediátrica, formación médica e investigación, con personal suficiente y capacitado.',
                    '<img decoding="async" width="200" class="elemento_interno" src="F4.jpg" alt="">',
                    '<b>También puedes consultar</b>'
                    '\n<button class="info" onclick="Mostrar(\'Historia\')">Historia</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Valores\')">Valores</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Aniversario\')">Aniversario</button><b> </b>'              
                ]
            elif Intento['tag'] == "valores":
                return [
                    Respuesta,
                    '<b>También puedes consultar</b>'
                    '\n<button class="info" onclick="Mostrar(\'Historia\')">Historia</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Misión y Visión\')">Misión y Visión</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Aniversario\')">Aniversario</button><b> </b>' 
                ]
            elif Intento['tag'] == "elevador":
                return [
                    Respuesta,
                    '<img decoding="async" width="300" class="elemento_interno" src="E.png" alt="">',
                    '<b>En Caso de Emergencia</b>'
                    '\nComunícate al area de <b>Mantenimiento</b> o a la empresa <b>KONE</b> México elevadores. Recuerda mantener la calma y comunicarte a los números de atención.'
                    '\n<button class="infoArea" onclick="Mostrar(\'Mantenimiento\')">Mantenimiento</button><b> </b><a href="tel:8007027300"><button class="info"><b>KONE:</b> 800 702 73 00 📞</button></a>',
                    '<b>Pisos disponibles</b>'
                    '\n<button class="info" onclick="Mostrar(\'Planta Baja\')">Planta Baja</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Piso 1\')">Piso 1</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Piso 2\')">Piso 2</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Piso 3\')">Piso 3</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Piso 4\')">Piso 4</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Piso 5\')">Piso 5</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Piso 6\')">Piso 6</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Edificio Viejo\')">Edificio Viejo</button><b> </b>'
                ]
            elif Intento['tag'] == "farmacia":
                return generar_respuesta_area(nombre_area="Farmacia ", emoji="💊", piso="0", encargado="María Conchita Calderón Romero",
                    extensiones=[("Farmacia", "7041"), ("Farmacia Oficina", "7042")]
                )
            elif Intento['tag'] == "alianza_estrategica":
                return generar_respuesta_area(nombre_area="Alianza Estratégica ", emoji="🙏", piso="6", encargado="L.C.C Jesús Francisco Herrera Martínez",
                    extensiones=[("Alianza Estratégica", "7004")]
                )
            elif Intento['tag'] == "almacen_general":
                return generar_respuesta_area(nombre_area="Almacén General y Activos fijos ", emoji="💉", piso="0", encargado="C. Olga Lucero Pimental Labrada",
                    extensiones=[("Almacén General", "7005")]
                )
            elif Intento['tag'] == "sub_almacen":
                return generar_respuesta_area(nombre_area="Sub Almacén ", emoji="💉", piso="5", encargado="",
                    extensiones=[("Sub Almacén", "7006")]
                )
            elif Intento['tag'] == "apoyo_nutricional":
                return generar_respuesta_area(nombre_area="Apoyo Nutricional ", emoji="🍎", piso="2", encargado="Lm. Helen Gaxiola Lizárraga",
                    extensiones=[("Apoyo Nutricional", "7007")]
                )
            elif Intento['tag'] == "archivo_clinico":
                return generar_respuesta_area(nombre_area="Archivo Clínico ", emoji="📂", piso="2", encargado="Lic. Dalia Ramírez Morales",
                    extensiones=[("Archivo Clínico", "7008")]
                )
            elif Intento['tag'] == "biomedica_ingenieria":
                return generar_respuesta_area(nombre_area="Biomédica Ingeniería ", emoji="🔩", piso="1", encargado="Ing. Jorge Luis Baez Vargas",
                    extensiones=[("Biomédica Ingeniería", "7011")]
                )
            elif Intento['tag'] == "calidad":
                return generar_respuesta_area(nombre_area="Calidad Hospitalaria ", emoji="🏥", piso="6", encargado="Enf. Fabiola Sánchez Mapula",
                    extensiones=[("Calidad Hospitalaria", "7012")]
                )
            elif Intento['tag'] == "cardiologia":
                return generar_respuesta_area(nombre_area="Cardiología ", emoji="🫀", piso="2", encargado="Dr. José Antonio Quibrera Matienzo",
                    extensiones=[("Cardiología", "7013")]
                )
            elif Intento['tag'] == "central_de_cuentas":
                return generar_respuesta_area(nombre_area="Central de Cuentas ", emoji="📋", piso="1", encargado="Lic. María Luisa Soto Vega",
                    extensiones=[("Central de Cuentas", "7014")]
                )
            elif Intento['tag'] == "centro_mezclas":
                return generar_respuesta_area(nombre_area="Centro de Mezclas ", emoji="💉", piso="7", encargado="Lic. Deyalinda Velasco Vela",
                    extensiones=[("Centro de Mezclas", "7015")]
                )
            elif Intento['tag'] == "ceye":
                return generar_respuesta_area(nombre_area="CEYE ", emoji="🥼", piso="5", encargado="Enf. Rosa Esthela Robles Uriarte",
                    extensiones=[("CEYE", "7016")]
                )
            elif Intento['tag'] == "cirugia":
                return generar_respuesta_area(nombre_area="Cirugía ", emoji="🩺", piso="5", encargado="Dr. Juan Manuel Zazueta Tirado",
                    extensiones=[("Cirugía", "7017"), ("Cirugía Oficina", "7018")]
                )
            elif Intento['tag'] == "clinica_heridas":
                return generar_respuesta_area(nombre_area="Clínica de Heridas ", emoji="🤕", piso="#", encargado="Enf. María Consuelo Chacón Zapién",
                    extensiones=[("Clínica de Heridas", "7019")]
                )
            elif Intento['tag'] == "cobranza":
                return generar_respuesta_area(nombre_area="Cobranza ", emoji="💸", piso="0", encargado="Gabriel Calderón Noriega",
                    extensiones=[("Cobranza", "7020")]
                )
            elif Intento['tag'] == "cocina":
                return generar_respuesta_area(nombre_area="Cocina ", emoji="🍽️", piso="2", encargado="Lic. Beatriz Elena Ibarra Yáñez",
                    extensiones=[("Cocina", "7021")]
                )
            elif Intento['tag'] == "consulta_externa":
                return [
                    f'<section class="card">'
                        f'<header>'
                            f'<p><b>Consulta Externa <span class="emoji3">👩‍⚕️</span></b> <b><button class="info pisos" onclick="Mostrar(\'Piso 2\')">Piso 2</button></b> </p>'
                            f'<p>Dra. Aleida López Barajas</p>'
                        f'</header>'
                    f'</section>',
                    Respuesta,
                    '<b>Teléfono Principal y Extensión</b>'
                    '\n<a href="tel:6677126606"><button class="info">6677126606 📞</button></a>'
                    '<b> </b><a href="tel:6677126606,7023"><button class="archivo"><b>Consulta Externa Recepción: </b>7023</button></a>'
                    '<b> </b><a href="tel:6677126606,7120"><button class="archivo"><b>Consulta Externa Jefe Pediátrico: </b>7120</button></a>'
                ]
            elif Intento['tag'] == "contabilidad_oficina":
                return generar_respuesta_area(nombre_area="Contabilidad ", emoji="💰", piso="6", encargado="",
                    extensiones=[("Contabilidad", "7024")]
                )
            elif Intento['tag'] == "dental":
                return generar_respuesta_area(nombre_area="Estomatología y Ortodoncia ", emoji="🦷", piso="2", encargado="Dra. Raquel Salazar Márquez",
                    extensiones=[("Estomatología y Ortodoncia", "7026")]
                )
            elif Intento['tag'] == "enfermeria":
                return [
                    f'<section class="card">'
                        f'<header>'
                            f'<p><b>Enfermería <span class="info emoji">👩‍⚕️</span></b> <b><button class="info pisos" onclick="Mostrar(\'Piso 6\')">Piso 6</button></b> </p>'
                        f'</header>'
                    f'</section>',
                    Respuesta,
                    '<b>Diferentes áreas de Enfermería</b>'
                    '\n<button class="info" onclick="Mostrar(\'Enfermería Enseñanza\')">Enf Enseñanza</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Enfermería Jefatura\')">Enf Jefatura</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Enfermería Subjefatura\')">Enf Subjefatura</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Especialidades Enfermería\')">Especialidades Enf</button><b> </b>'
                ]
            elif Intento['tag'] == "enfermeria_ensenanza":
                return generar_respuesta_area(nombre_area="Enfermería Enseñanza ", emoji="✏️", piso="6", encargado="Enf. Alba Berenice Madueño Madrigal ",
                    extensiones=[("Enfermería Enseñanza", "7029")]
                )
            elif Intento['tag'] == "enfermeria_jefatura":
                return generar_respuesta_area(nombre_area="Enfermería Jefatura ", emoji="👩‍⚕️", piso="6", encargado="",
                    extensiones=[("Enfermería Jefatura", "7030"), ("Enfermería Jefatura Secretaria", "7031")]
                )
            elif Intento['tag'] == "enfermeria_subjefatura":
                return generar_respuesta_area(nombre_area="Enfermería Subjefatura ", emoji="👩‍⚕️", piso="6", encargado="",
                    extensiones=[("Enfermería Subjefatura", "7032")]
                )
            elif Intento['tag'] == "ensenanza_medica":
                return [
                    f'<section class="card">'
                        f'<header>'
                            f'<p><b>Enseñanza Medica <span class="info emoji">🧑‍🏫</span></b> </p>'
                            f'<p>Dr. Alberto Paez Salazar \nEnf. Alba Berenice Madueño Madrigal</p>'
                        f'</header>'
                    f'</section>',
                    Respuesta,
                    '<b>Diferentes áreas de Enseñanza Medica</b>'
                    '\n<button class="info" onclick="Mostrar(\'Enseñanza Dos\')">Enseñanza Dos</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Enseñanza e Investigación\')">Enseñanza e Investigación</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Enseñanza Medica Jefe\')">Enseñanza Medica Jefe</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Enseñanza Medica Secretaría\')">Enseñanza Medica Secretaría</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Enseñanza Medicina Basada en Evidencias\')">Enseñanza Medicina Basada en Evidencias</button>'
                ]
            elif Intento['tag'] == "ensenanza_dos":
                return generar_respuesta_area(nombre_area="Enseñanza Dos ", emoji="📚", piso="4", encargado="Dr. Alberto Paez Salazar \nEnf. Alba Berenice Madueño Madrigal",
                    extensiones=[("Enseñanza Dos", "7033")]
                )
            elif Intento['tag'] == "ensenanza_investigacion":
                return generar_respuesta_area(nombre_area="Enseñanza e Investigación ", emoji="📖", piso="6", encargado="Dr. Alberto Paez Salazar \nEnf. Alba Berenice Madueño Madrigal",
                    extensiones=[("Enseñanza e Investigación", "7034")]
                )
            elif Intento['tag'] == "ensenanza_medica_jefe":
                return generar_respuesta_area(nombre_area="Enseñanza Medica Jefe ", emoji="👨‍⚕️", piso="4", encargado="Dr. Alberto Paez Salazar \nEnf. Alba Berenice Madueño Madrigal",
                    extensiones=[("Enseñanza Medica Jefe", "7035")]
                )
            elif Intento['tag'] == "secretaria_ensenanza_medica":
                return generar_respuesta_area(nombre_area="Enseñanza Medica Secretaría ", emoji="📋", piso="4", encargado="Dr. Alberto Paez Salazar \nEnf. Alba Berenice Madueño Madrigal",
                    extensiones=[("Enseñanza Medica Secretaría", "7036")]
                )
            elif Intento['tag'] == "medicina_basada_evidencias":
                return generar_respuesta_area(nombre_area="Enseñanza Medicina Basada en Evidencias ", emoji="📊", piso="4", encargado="Dr. Alberto Paez Salazar \nEnf. Alba Berenice Madueño Madrigal",
                    extensiones=[("Enseñanza Medicina Basada en Evidencias", "7037")]
                )
            elif Intento['tag'] == "epidemiologia":
                return generar_respuesta_area(nombre_area="Epidemiologia ", emoji="🦠", piso="2", encargado="Ep. Rosalino Flores Rocha",
                    extensiones=[("Epidemiologia", "7040")]
                )
            elif Intento['tag'] == "gastroenterologia":
                return generar_respuesta_area(nombre_area="Gastroenterología ", emoji="🥼", piso="2", encargado="Dra. Vianey Paola Zamudio Vázquez",
                    extensiones=[("Gastroenterología", "7044"), ("Gastroenterología Oficina", "7044")]
                )
            elif Intento['tag'] == "quirofano_endoscopia":
                return generar_respuesta_area(nombre_area="Quirófano de endoscopia ", emoji="🩺", piso="3", encargado="Enf. Ángelica Vega Millán",
                    extensiones=[("Quirófano de endoscopia", "7043")]
                )
            elif Intento['tag'] == "genetica":
                return generar_respuesta_area(nombre_area="Genetica ", emoji="🧬", piso="1", encargado="Dr. Jesús Ernesto Dueñas Arias",
                    extensiones=[("Genetica", "7045")]
                )
            elif Intento['tag'] == "infectologia":
                return generar_respuesta_area(nombre_area="Infectología ", emoji="🦠", piso="5", encargado="Dr. Carlos Alberto Velázquez Ríos<br>Enf. Nancy Rebeca Díaz Beltrán ",
                    extensiones=[("Infectología Oficina", "7046"), ("Infectología Sala", "7047")]
                )
            elif Intento['tag'] == "informatica":
                return generar_respuesta_area(nombre_area="Informática ", emoji="💻", piso="6", encargado="Lic. Jorge Antonio Cruz Sainz",
                    extensiones=[("Informática Jefe", "7048"), ("Informática Oficina", "7010")]
                )
            elif Intento['tag'] == "informes_recepcion":
                return generar_respuesta_area(nombre_area="Informes Recepción ", emoji="☎️", piso="0", encargado="",
                    extensiones=[("Informes Recepción", "7049")]
                )
            elif Intento['tag'] == "inhaloterapia":
                return generar_respuesta_area(nombre_area="Inhaloterapia ", emoji="👃", piso="0", encargado="Enf. Ana Guadalupe Cruz Castillo \nDra. Ana María  López Reyes",
                    extensiones=[("Inhaloterapia", "7050")]
                )
            elif Intento['tag'] == "juridico":
                return generar_respuesta_area(nombre_area="Juridico ", emoji="🏛️", piso="6", encargado="Elizabeth Gomez Olivarez",
                    extensiones=[("Juridico", "7051")]
                )
            elif Intento['tag'] == "laboratorio":
                return generar_respuesta_area(nombre_area="Laboratorio ", emoji="🔬", piso="1", encargado="QFB. Maria Leticia Félix Miranda",
                    extensiones=[("Laboratorio Recepción C.E.", "7052"), ("Laboratorio Filtro HOSP", "7030"), ("Laboratorio Jefe", "7031")]
                )
            elif Intento['tag'] == "mantenimiento":
                return generar_respuesta_area(nombre_area="Mantenimiento ", emoji="🛠️", piso="1", encargado="Ing. Jesús Enrique Rubio Medina",
                    extensiones=[("Mantenimiento Oficina", "7053"), ("Mantenimiento", "7054")]
                )
            elif Intento['tag'] == "medicina_interna":
                return generar_respuesta_area(nombre_area="Medicina Interna ", emoji="⚕️", piso="5", encargado="Enf. María del Rosario Chamorro Chairez",
                    extensiones=[("Medicina Interna", "7055")]
                )
            elif Intento['tag'] == "medicina_legal":
                return generar_respuesta_area(nombre_area="Medicina Legal ", emoji="⚖️", piso="6", encargado="Dra. Ana Luisa Castro Medina",
                    extensiones=[("Medicina Legal", "7056")]
                )
            elif Intento['tag'] == "medicina_preventiva":
                return generar_respuesta_area(nombre_area="Medicina Preventiva ", emoji="🩺", piso="2", encargado="Enf. Silvia Viridiana Angulo Leyva",
                    extensiones=[("Medicina Preventiva", "7057")]
                )
            elif Intento['tag'] == "medicina_transfusional":
                return generar_respuesta_area(nombre_area="Medicina Transfusional ", emoji="🩸", piso="#", encargado="Enf. Favela Bernal Jessica Lizbeth",
                    extensiones=[("Medicina Transfusional", "7058")]
                )
            elif Intento['tag'] == "modulo_informacion":
                return generar_respuesta_area(nombre_area="Modulo de Información ", emoji="📒", piso="0", encargado="",
                    extensiones=[("Modulo de Información", "7059")]
                )
            elif Intento['tag'] == "neonatologia":
                return generar_respuesta_area(nombre_area="Neonatología ", emoji="👶", piso="5", encargado="Dra. Aleyda Zazueta Chávez<br>Enf. Sandra Elena Benítez López",
                    extensiones=[("Neonatología Infecto", "7060"), ("Neonatología Oficina", "7061"), ("Neonatología Sala", "7062")]
                )
            elif Intento['tag'] == "oncologia":
                return [
                    f'<section class="card">'
                        f'<header>'
                            f'<p><b>Oncología <span class="info emoji">💊</span></b> <b><button class="info pisos" onclick="Mostrar(\'Edificio Viejo\')">Edificio Viejo</button></b> </p>'
                            f'<p>Dra. Obdilia Gutiérrez Guzmán</p>'
                        f'</header>'
                    f'</section>',
                    Respuesta,
                    '<b>Diferentes áreas de Oncología</b>'
                    '\n<button class="info" onclick="Mostrar(\'Oncología Angelita\')">Oncología Angelita</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Oncología Banco de Sangre\')">Onco Banco de Sangre</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Oncología Catéteres\')">Onco Catéteres</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Oncología Jefatura\')">Onco Jefatura</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Oncología Jefe\')">Onco Jefe</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Oncología Oficina Hematología\')">Onco Oficina Hematología</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Oncología Oficina Secretaría\')">Onco Oficina Secretaría</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Oncología Quimioterapia Ambulatoria\')">Onco Quimioterapia Ambulatoria</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Oncología Recepción Consulta\')">Onco Recepción Consulta</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Oncología Residentes\')">Onco Residentes</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Oncología TS Hospitalización\')">Onco TS Hospitalización</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Oncología Somatometría\')">Onco Somatometría</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Oncología Tumores\')">Onco Tumores</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Oncología Sala\')">Onco Sala</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Nutrición Onco Pediátrico\')">Nutrición Onco Pediátrico</button>'
                ]
            elif Intento['tag'] == "oncologia_angelita":
                return generar_respuesta_area(nombre_area="Oncología Angelita ", emoji="🏥", piso="7", encargado="Dra. Obdilia Gutiérrez Guzmán",
                    extensiones=[("Oncología Angelita", "7064")]
                )
            elif Intento['tag'] == "oncologia_banco_sangre":
                return generar_respuesta_area(nombre_area="Oncología Banco de Sangre ", emoji="🩸", piso="7", encargado="Dr. Altamirano Álvarez Eduardo",
                    extensiones=[("Oncología Banco de Sangre", "7065")]
                )
            elif Intento['tag'] == "oncologia_cateteres":
                return generar_respuesta_area(nombre_area="Oncología Catéteres ", emoji="🥼", piso="7", encargado="Dra. Obdilia Gutiérrez Guzmán",
                    extensiones=[("Oncología Catéteres", "7066")]
                )
            elif Intento['tag'] == "oncologia_jefatura":
                return generar_respuesta_area(nombre_area="Oncología Jefatura ", emoji="🗃️", piso="7", encargado="Dra. Obdilia Gutiérrez Guzmán",
                    extensiones=[("Oncología Jefatura", "7067")]
                )
            elif Intento['tag'] == "oncologia_jefe":
                return generar_respuesta_area(nombre_area="Oncología Jefe ", emoji="🧑‍⚕️", piso="7", encargado="Dra. Obdilia Gutiérrez Guzmán",
                    extensiones=[("Oncología Jefe", "7068")]
                )
            elif Intento['tag'] == "oncologia_oficina_hematologia":
                return generar_respuesta_area(nombre_area="Oncología Oficina Hematología ", emoji="🩸", piso="7", encargado="Dr. Altamirano Álvarez Eduardo",
                    extensiones=[("Oncología Oficina Hematología", "7070")]
                )
            elif Intento['tag'] == "oncologia_oficina_secretaria":
                return generar_respuesta_area(nombre_area="Oncología Oficina Secretaría ", emoji="🗃️", piso="7", encargado="Dra. Obdilia Gutiérrez Guzmán",
                    extensiones=[("Oncología Oficina Secretaría", "7071")]
                )
            elif Intento['tag'] == "oncologia_quimioterapia_amb":
                return generar_respuesta_area(nombre_area="Oncología Quimioterapia Ambulatoria ", emoji="💉", piso="7", encargado="Dra. Obdilia Gutiérrez Guzmán",
                    extensiones=[("Oncología Quimioterapia AMB", "7072")]
                )
            elif Intento['tag'] == "oncologia_recepcion_consulta":
                return generar_respuesta_area(nombre_area="Oncología Recepción Consulta ", emoji="📋", piso="7", encargado="Dra. Obdilia Gutiérrez Guzmán",
                    extensiones=[("Oncología Recepción Consulta", "7073")]
                )
            elif Intento['tag'] == "oncologia_residentes":
                return generar_respuesta_area(nombre_area="Oncología Residentes ", emoji="👩‍⚕️", piso="7", encargado="Dra. Obdilia Gutiérrez Guzmán",
                    extensiones=[("Oncología Residentes", "7074")]
                )
            elif Intento['tag'] == "oncologia_ts_hospitalizacion":
                return generar_respuesta_area(nombre_area="Oncología TS Hospitalización ", emoji="🏥", piso="7", encargado="Dra. Obdilia Gutiérrez Guzmán",
                    extensiones=[("Oncología TS Hospitalización", "7075")]
                )
            elif Intento['tag'] == "oncologia_somatometria":
                return generar_respuesta_area(nombre_area="Oncología Somatometría ", emoji="📏", piso="7", encargado="Dra. Obdilia Gutiérrez Guzmán",
                    extensiones=[("Oncología Somatometría", "7118")]
                )
            elif Intento['tag'] == "oncologia_tumores":
                return generar_respuesta_area(nombre_area="Oncología Tumores ", emoji="⛑️", piso="7", encargado="Dra. Obdilia Gutiérrez Guzmán",
                    extensiones=[("Oncología Tumores", "7119")]
                )
            elif Intento['tag'] == "oncologia_sala":
                return generar_respuesta_area(nombre_area="Oncología Sala ", emoji="🏥", piso="7", encargado="Dra. Obdilia Gutiérrez Guzmán",
                    extensiones=[("Oncología Sala", "7122")]
                )
            elif Intento['tag'] == "nutricion_onco_pediatrico":
                return generar_respuesta_area(nombre_area="Nutrición Onco Pediátrico ", emoji="🍎", piso="7", encargado="Dra. Obdilia Gutiérrez Guzmán",
                    extensiones=[("Nutrición Onco Pediátrico", "7125")]
                )
            elif Intento['tag'] == "anatomia_patologica":
                return generar_respuesta_area(nombre_area="Patológia ", emoji="🧬", piso="3", encargado="Pat. Eri Peña Martínez",
                    extensiones=[("Patológia", "7077")]
                )
            elif Intento['tag'] == "quirofano_1_2":
                return generar_respuesta_area(nombre_area="Quirófano 1 y 2 ", emoji="⚕️", piso="#", encargado="Dr. Jesús Oscar Soto Quintero",
                    extensiones=[("Quirófano 1 y 2", "7078")]
                )
            elif Intento['tag'] == "rayos_x":
                return generar_respuesta_area(nombre_area="Rayos X ", emoji="🩻", piso="1", encargado="Dr. José Guadalupe Mendoza Flores",
                    extensiones=[("Rayos X Placas", "7080"), ("Rayos X Oficina Mayte", "7081"), ("Recepción Rayos X", "7115"),
                                    ("Ultrasonido Rayos X", "7116"), ("Rayos X TAC", "7117")]
                )
            elif Intento['tag'] == "recursos_financieros":
                return generar_respuesta_area(nombre_area="Recursos Financieros ", emoji="💵", piso="6", encargado="Lic. Marlenne Karime Osuna Bolado",
                    extensiones=[("Recursos Financieros", "7082")]
                )
            elif Intento['tag'] == "recursos_humanos":
                return generar_respuesta_area(nombre_area="Recursos Humanos ", emoji="👨‍⚕️", piso="6", encargado="Lic. Hermelinda Avendaño Gutiérrez",
                    extensiones=[("Recursos Humanos", "7083"), ("Recursos Humanos Jefe", "7084"), ("Recursos Humanos Contrato", "7103")]
                )
            elif Intento['tag'] == "seguro_popular":
                return generar_respuesta_area(nombre_area="Seguro Popular ", emoji="🧑‍⚕️", piso="#", encargado="Lic. María de los Ángeles López López",
                    extensiones=[("Seguro Popular Medico", "7085"), ("Seguro Popular Oficina", "7086")]
                )
            elif Intento['tag'] == "servicios_generales":
                return generar_respuesta_area(nombre_area="Servicios Generales ", emoji="🧹", piso="0", encargado="Ing. Jose Luis Ochoa Arellano",
                    extensiones=[("Servicios Generales", "7087")]
                )
            elif Intento['tag'] == "subdireccion":
                return [
                    f'<section class="card">'
                        f'<header>'
                            f'<p><b>Subdirección <span class="info emoji">🏦</span></b> <b><button class="info pisos" onclick="Mostrar(\'Piso 6\')">Piso 6</button></b> </p>'
                        f'</header>'
                    f'</section>',
                    Respuesta,
                    '<b>Diferentes áreas de Subdirección</b>'
                    '\n<button class="info" onclick="Mostrar(\'Subdirección de Planeación\')">Sub de Planeación</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Subdirección de Servicios Auxiliares\')">Sub de Servicios Auxiliares</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Subdirección Médica\')">Sub Médica</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Subdirección Secretaría\')">Sub Secretaría</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Subdirección Administrativa SEC\')">Sub Administrativa SEC</button>'
                ]
            elif Intento['tag'] == "subdireccion_planeacion":
                return generar_respuesta_area(nombre_area="Subdirección de Planeación ", emoji="📋", piso="6", encargado="M. Iván Rafael Mendoza Zuñiga",
                    extensiones=[("Subdirección de Planeación", "7088")]
                )
            elif Intento['tag'] == "subdireccion_servicios_auxiliares":
                return generar_respuesta_area(nombre_area="Subdirección Servicios Auxiliares ", emoji="🖼️", piso="6", encargado=" Dra. Cynthia Gabriela Torres Galicia",
                    extensiones=[("Subdirección Servicios Auxiliares", "7089")]
                )
            elif Intento['tag'] == "subdireccion_medica":
                return generar_respuesta_area(nombre_area="Subdirección Medica ", emoji="🥼", piso="6", encargado="Dr. Fernando de Jesús  Bodart Román<br>Dra. Laura Elena Salazar Castro",
                    extensiones=[("Subdirección Medica", "7090")]
                )
            elif Intento['tag'] == "subdireccion_secretaria":
                return generar_respuesta_area(nombre_area="Subdirección Secretaria ", emoji="✒️", piso="6", encargado="",
                    extensiones=[("Subdirección Secretaria", "7091")]
                )
            elif Intento['tag'] == "terapia_intensiva":
                return generar_respuesta_area(nombre_area="Terapia Intensiva ", emoji="❤️‍🩹", piso="4", encargado="Dra. Vianey Melchor García<br>Enf. Soledad Ibarra Yáñez ",
                    extensiones=[("Terapia Intensiva Oficina", "7092"), ("Terapia Intensiva Sala", "7093")]
                )
            elif Intento['tag'] == "trabajo_social":
                return [
                    f'<section class="card">'
                        f'<header>'
                            f'<p><b>Trabajo Social <span class="info emoji">💼</span></b>'
                            f'<p>Lic. Maria de la Cruz Olguín Mendoza</p>'
                        f'</header>'
                    f'</section>',
                    Respuesta,
                    '<b>Diferentes áreas de Trabajo Social</b>'
                    '\n<button class="info" onclick="Mostrar(\'Trabajo Social Infectología\')">TS Infectología</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Trabajo Social Neonatología\')">TS Neonatología</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Trabajo Social Oficina\')">TS Oficina</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Trabajo Social Qx Ambulatorio\')">TS QX Ambulatorio</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Trabajo Social Terapia Intensiva\')">TS Terapia Intensiva</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Trabajo Social Urgencias\')">TS Urgencias</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Trabajo Social Jefatura\')">TS Jefatura</button>'
                ]
            elif Intento['tag'] == "trabajo_social_infectologia":
                return generar_respuesta_area(nombre_area="Trabajo Social Infectología ", emoji="🦠", piso="5", encargado="",
                    extensiones=[("Trabajo Social Infectología", "7094")]
                )
            elif Intento['tag'] == "trabajo_social_neonatologia":
                return generar_respuesta_area(nombre_area="Trabajo Social Neonatología ", emoji="👶", piso="5", encargado="",
                    extensiones=[("Trabajo Social Neonatología", "7095")]
                )
            elif Intento['tag'] == "trabajo_social_oficina":
                return generar_respuesta_area(nombre_area="Trabajo Social Oficina ", emoji="🏢", piso="0", encargado="",
                    extensiones=[("Trabajo Social Oficina", "7096")]
                )
            elif Intento['tag'] == "trabajo_social_qx_ambulatorio":
                return generar_respuesta_area(nombre_area="Trabajo Social QX Ambulatorio ", emoji="🚑", piso="3", encargado="",
                    extensiones=[("Trabajo Social QX Ambulatorio", "7097")]
                )
            elif Intento['tag'] == "trabajo_social_terapia_intensiva":
                return generar_respuesta_area(nombre_area="Trabajo Social Terapia Intensiva ", emoji="💪", piso="4", encargado="",
                    extensiones=[("Trabajo Social Terapia Intensiva", "7098")]
                )
            elif Intento['tag'] == "trabajo_social_urgencias":
                return generar_respuesta_area(nombre_area="Trabajo Social Urgencias ", emoji="⏰", piso="0", encargado="",
                    extensiones=[("Trabajo Social Urgencias", "7099")]
                )
            elif Intento['tag'] == "trabajo_social_jefatura":
                return generar_respuesta_area(nombre_area="Trabajo Social Jefatura ", emoji="👩‍⚕️", piso="0", encargado="",
                    extensiones=[("Trabajo Social Jefatura", "7114")]
                )
            elif Intento['tag'] == "urgencias":
                return generar_respuesta_area(nombre_area="Urgencias ", emoji="🚑", piso="0", encargado="Dr. Edgardo Tostado Morales<br>Enf. Alejandra Osuna Garcia",
                    extensiones=[("Urgencias Oficina", "7100"), ("Urgencias Sala", "7101"), ("Caja Urgencias Pediátrico", "7109"), ("JEF Urgencias Pediátrico", "7110")]
                )
            elif Intento['tag'] == "vigilancia_camilleros":
                return generar_respuesta_area(nombre_area="Vigilancia-Camilleros ", emoji="😷", piso="0", encargado="",
                    extensiones=[("Vigilancia-Camilleros", "7102")]
                )
            elif Intento['tag'] == "insabi":
                return generar_respuesta_area(nombre_area="INSABI ", emoji="🏥", piso="0", encargado="Dra. Maria Luisa Rodríguez León ",
                    extensiones=[("INSABI", "7104")]
                )
            elif Intento['tag'] == "banco_sangre_ts":
                return generar_respuesta_area(nombre_area="Banco de Sangre ", emoji="🩸", piso="1", encargado="Dr. Francisco Sazueta Quintero ",
                    extensiones=[("Banco de Sangre TS", "7105")]
                )
            elif Intento['tag'] == "adquisiciones":
                return generar_respuesta_area(nombre_area="Adquisiciones ", emoji="📦", piso="#", encargado="Lic. Manuela Collantes García ",
                    extensiones=[("Adquisiciones", "7106")]
                )
            elif Intento['tag'] == "soporte_tecnico":
                return generar_respuesta_area(nombre_area="Soporte Técnico ", emoji="🖥️", piso="0", encargado="Ing. Jorge Antonio Cruz Sainz",
                    extensiones=[("Soporte Técnico", "7108")]
                )
            elif Intento['tag'] == "subdireccion_administrativa_sec":
                return generar_respuesta_area(nombre_area="Subdirección Administrativa Sec ", emoji="🏦", piso="6", encargado="",
                    extensiones=[("Subdirección Administrativa Sec", "7111")]
                )
            elif Intento['tag'] == "surt_recetas":
                return generar_respuesta_area(nombre_area="Surtimiento de Recetas ", emoji="💊", piso="5", encargado="María Conchita Calderón Romero",
                    extensiones=[("Surtimiento de Recetas", "7112")]
                )
            elif Intento['tag'] == "investigacion_medica":
                return generar_respuesta_area(nombre_area="Investigación Medica ", emoji="🔬", piso="1", encargado="Dr. Alberto Paez Salazar ",
                    extensiones=[("Investigación Medica", "7121")]
                )
            elif Intento['tag'] == "programa_vih":
                return generar_respuesta_area(nombre_area="Programa VIH ", emoji="⛑️", piso="#", encargado="",
                    extensiones=[("Programa VIH", "7123")]
                )
            elif Intento['tag'] == "hemodialisis":
                return generar_respuesta_area(nombre_area="Hemodiálisis ", emoji="❤️‍🩹", piso="3", encargado="Dra. Iyali Margarita Corrales Cambero \nEnf. Scanda María Ureta Camacho",
                    extensiones=[("Hemodiálisis", "7124")]
                )
            elif Intento['tag'] == "qx":
                return [
                    f'<section class="card">'
                        f'<header>'
                            f'<p><b>Quirofano (QX) <span class="info emoji">😷</span></b> <b><button class="info pisos" onclick="Mostrar(\'Piso 3\')">Piso 3</button></b> </p>'
                        f'</header>'
                    f'</section>',
                    Respuesta,
                    '<b>Diferentes áreas de Quirofano (QX)</b>'             
                    '\n<button class="info" onclick="Mostrar(\'Trabajo Social Qx Ambulatorio\')">TS QX Ambulatorio</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Admisión QX\')">Admisión QX</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Admisión Qx Ambulatorio\')">Admisión Qx Ambulatorio</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Quirófano 1 y 2\')">Quirófano 1 y 2</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Jefe Qx Pediátrico\')">Jefe Qx Pediátrico</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Piso3 Qx Amm\')">Piso3 Qx Amm</button><b> </b>'
                ]
            elif Intento['tag'] == "admisiones_qx":
                return generar_respuesta_area(nombre_area="Admisión QX ", emoji="💉", piso="3", encargado="",
                    extensiones=[("Admisión QX", "7113")]
                )
            elif Intento['tag'] == "admision_qx_ambulatorio":
                return generar_respuesta_area(nombre_area="Admisión Qx Ambulatorio ", emoji="💊", piso="3", encargado="",
                    extensiones=[("Admisión Qx Ambulatorio", "7127")]
                )
            elif Intento['tag'] == "jefe_qx_pediatrico":
                return generar_respuesta_area(nombre_area="Jefe Qx Pediátrico ", emoji="👨‍⚕️", piso="3", encargado="",
                    extensiones=[("Jefe Qx Pediátrico", "7128")]
                )
            elif Intento['tag'] == "piso3_qx_amm":
                return generar_respuesta_area(nombre_area="Piso3 Qx Amm ", emoji="🏥", piso="3", encargado="",
                    extensiones=[("Piso3 Qx Amm", "7132")]
                )
            elif Intento['tag'] == "residentes_cirugia":
                return generar_respuesta_area(nombre_area="Residentes Cirugía ", emoji="👨‍⚕️", piso="#", encargado="",
                    extensiones=[("Residentes Cirugía of Pediatrico", "7126")]
                )
            elif Intento['tag'] == "banco_de_leche":
                return generar_respuesta_area(nombre_area="Banco de Leche ", emoji="🍼", piso="2", encargado="",
                    extensiones=[("Banco de Leche", "7129")]
                )
            elif Intento['tag'] == "piso_1":
                return [
                    f'<section class="card">'
                        f'<header>'
                            f'<p><span class="info emoji">🏢</span> <b><button class="info pisosT" onclick="Mostrar(\'Piso 1\')">Piso 1</button></b> <span class="info emoji">🏢</span></p>'
                        f'</header>'
                    f'</section>',
                    Respuesta,
                    '<b>Diferentes áreas del Piso 1</b>'
                    '\n<button class="info" onclick="Mostrar(\'Biomédica Ingeniería\')">Biomédica Ingeniería</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Genetica\')">Genetica</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Laboratorio\')">Laboratorio</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Mantenimiento\')">Mantenimiento</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Rayos X\')">Rayos X</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Banco de Sangre\')">Banco de Sangre</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Investigación Medica\')">Investigación Medica</button><b> </b>'
                ]
            elif Intento['tag'] == "piso_2":
                return [
                    f'<section class="card">'
                        f'<header>'
                            f'<p><span class="info emoji">🏢</span> <b><button class="info pisosT" onclick="Mostrar(\'Piso 2\')">Piso 2</button></b> <span class="info emoji">🏢</span></p>'
                        f'</header>'
                    f'</section>',
                    Respuesta,
                    '<b>Diferentes áreas del Piso 2</b>'
                    '\n<button class="info" onclick="Mostrar(\'Apoyo Nutricional\')">Apoyo Nutricional</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Archivo Clínico\')">Archivo Clínico</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Cardiología\')">Cardiología</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Cocina\')">Cocina</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Consulta Externa\')">Consulta Externa</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Estomatología y Ortodoncia\')">Estomatología y Ortodoncia</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Epidemiologia\')">Epidemiologia</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Gastroenterología\')">Gastroenterología</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Banco de Leche\')">Banco de Leche</button><b> </b>'
                ]
            elif Intento['tag'] == "piso_3":
                return [
                    f'<section class="card">'
                        f'<header>'
                            f'<p><span class="info emoji">🏢</span> <b><button class="info pisosT" onclick="Mostrar(\'Piso 3\')">Piso 3</button></b> <span class="info emoji">🏢</span></p>'
                        f'</header>'
                    f'</section>',
                    Respuesta,
                    '<b>Diferentes áreas del Piso 3</b>'
                    '\n<button class="info" onclick="Mostrar(\'Quirófano de endoscopia\')">Quirófano de endoscopia</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Patológia\')">Patológia</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Trabajo Social QX Ambulatorio\')">Trabajo Social QX Ambulatorio</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Hemodiálisis\')">Hemodiálisis</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Admisión QX\')">Admisión QX</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Admisión Qx Ambulatorio \')">Admisión Qx Ambulatorio</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Jefe Qx Pediátrico\')">Jefe Qx Pediátrico</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Piso3 Qx Amm\')">Piso3 Qx Amm</button><b> </b>'
                ]
            elif Intento['tag'] == "piso_4":
                return [
                    f'<section class="card">'
                        f'<header>'
                            f'<p><span class="info emoji">🏢</span> <b><button class="info pisosT" onclick="Mostrar(\'Piso 4\')">Piso 4</button></b> <span class="info emoji">🏢</span></p>'
                        f'</header>'
                    f'</section>',
                    Respuesta,
                    '<b>Diferentes áreas del Piso 4</b>'
                    '\n<button class="info" onclick="Mostrar(\'Enseñanza e Investigación Medica \')">Enseñanza e Investigación Medica </button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Terapia Intensiva\')">Terapia Intensiva</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Trabajo Social Terapia Intensiva\')">Trabajo Social Terapia Intensiva</button><b> </b>'
                ]
            elif Intento['tag'] == "piso_5":
                return [
                    f'<section class="card">'
                        f'<header>'
                            f'<p><span class="info emoji">🏢</span> <b><button class="info pisosT" onclick="Mostrar(\'Piso 5\')">Piso 5</button></b> <span class="info emoji">🏢</span></p>'
                        f'</header>'
                    f'</section>',
                    Respuesta,
                    '<b>Diferentes áreas del Piso 5</b>'
                    '\n<button class="info" onclick="Mostrar(\'Sub Almacén\')">Sub Almacén</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'CEYE\')">CEYE</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Infectología\')">Infectología</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Medicina Interna\')">Medicina Interna</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Neonatología\')">Neonatología</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Trabajo Social Infectología\')">Trabajo Social Infectología</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Trabajo Social Neonatología\')">Trabajo Social Neonatología</button><b> </b>'
                ]
            elif Intento['tag'] == "piso_6":
                return [
                    f'<section class="card">'
                        f'<header>'
                            f'<p><span class="info emoji">🏢</span> <b><button class="info pisosT" onclick="Mostrar(\'Piso 6\')">Piso 6</button></b> <span class="info emoji">🏢</span></p>'
                        f'</header>'
                    f'</section>',
                    Respuesta,
                    '<b>Diferentes áreas del Piso 6</b>'
                    '\n<button class="info" onclick="Mostrar(\'Alianza Estratégica\')">Alianza Estratégica</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Aula de Capacitación\')">Aula de Capacitación</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Calidad Hospitalaria\')">Calidad Hospitalaria</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Contabilidad\')">Contabilidad</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Enfermería Enseñanza\')">Enfermería Enseñanza</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Enfermería Jefatura\')">Enfermería Jefatura</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Enfermería Subjefatura\')">Enfermería Subjefatura</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Enseñanza Dos\')">Enseñanza Dos</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Informática\')">Informática</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Juridico\')">Juridico</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Medicina Legal\')">Medicina Legal</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Recursos Financieros\')">Recursos Financieros</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Recursos Humanos\')">Recursos Humanos</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Subdirección de Planeación\')">Subdirección de Planeación</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Subdirección Servicios Auxiliares\')">Subdirección Servicios Auxiliares</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Subdirección Medica\')">Subdirección Medica</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Subdirección Secretaria\')">Subdirección Secretaria</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Subdirección Administrativa Sec\')">Subdirección Administrativa Sec</button><b> </b>'
                ]
            elif Intento['tag'] == "planta_baja":
                return [
                    f'<section class="card">'
                        f'<header>'
                            f'<p><span class="info emoji">🏢</span> <b><button class="info pisosT" onclick="Mostrar(\'Planta Baja\')">Planta Baja</button></b> <span class="info emoji">🏢</span></p>'
                        f'</header>'
                    f'</section>',
                    Respuesta,
                    '<b>Diferentes áreas de la Planta Baja</b>'
                    '\n<button class="info" onclick="Mostrar(\'Farmacia\')">Farmacia</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Almacen General\')">Almacén General</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Informes Recepcion\')">Informes Recepción</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Inhaloterapia\')">Inhaloterapia</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Terapia Respiratoria\')">Terapia Respiratoria</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Modulo de Informacion\')">Módulo de Información</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Servicios Generales\')">Servicios Generales</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Trabajo Social Oficina\')">Trabajo Social Oficina</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Trabajo Social Urgencias\')">Trabajo Social Urgencias</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Trabajo Social Jefatura\')">Trabajo Social Jefatura</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Urgencias\')">Urgencias</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'INSABI\')">INSABI</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Soporte Tecnico\')">Soporte Técnico</button><b> </b>'
                ]
            elif Intento['tag'] == "edificio_viejo":
                return [
                    f'<section class="card">'
                        f'<header>'
                            f'<p><span class="info emoji">🏢</span> <b><button class="info pisosT" onclick="Mostrar(\'Edificio Viejo\')">Edificio Viejo</button></b> <span class="info emoji">🏢</span></p>'
                        f'</header>'
                    f'</section>',
                    Respuesta,
                    '<b>Diferentes áreas del Edificio Viejo</b>'
                    '\n<button class="info" onclick="Mostrar(\'Oncología Angelita\')">Oncología Angelita</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Oncología Banco de Sangre\')">Oncología Banco de Sangre</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Oncología Catéteres\')">Oncología Catéteres</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Oncología Jefatura\')">Oncología Jefatura</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Oncología Jefe\')">Oncología Jefe</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Oncología Oficina Hematología\')">Oncología Oficina Hematología</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Oncología Oficina Secretaría\')">Oncología Oficina Secretaría</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Oncología Quimioterapia Ambulatoria\')">Oncología Quimioterapia Ambulatoria</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Oncología Recepción Consulta\')">Oncología Recepción Consulta</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Oncología Residentes\')">Oncología Residentes</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Oncología TS Hospitalización\')">Oncología TS Hospitalización</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Oncología Somatometría\')">Oncología Somatometría</button><b> </b>'
                    '<button class="infoArea" onclick="Mostrar(\'Oncología Tumores\')">Oncología Tumores</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Oncología Sala\')">Oncología Sala</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Nutrición Onco Pediátrico\')">Nutrición Onco Pediátrico</button>'
                ]
            return [Respuesta]
    return ["Lo siento, no entendí tu pregunta."]