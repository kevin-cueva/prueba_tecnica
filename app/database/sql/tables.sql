
CREATE TABLE IF NOT EXISTS especies_marinas( -- crea la especies_marinas si no existe 
-- Esta tabla es para manejar las tareas del usuario
    id_especies_marinas INTEGER PRIMARY KEY, --llave primaria 
    lugar TEXT NO NULL, --texto
    especie TEXT NO NULL, -- texto
    avistamiento TEXT NO NULL, -- texto
    created_date TEXT, -- la fecha de creacion
    created_time TEXT -- el tiempo de los datos
);

        CREATE TABLE IF NOT EXISTS lugares ( -- crea la tabla lugares si no esxiste
            id_lugar INTEGER PRIMARY KEY, --llave primaria 
            pais TEXT NO NULL,
            departamento TEXT NO NULL, -- texto
            ciudad TEXT NO NULL, -- texto
            nombre_del_lugar TEXT NO NULL,
            --FOREIGN KEY (nombre_del_lugar) REFERENCES especies_marinas(lugar) -- llave foranea con lugar
            FOREIGN KEY (id_lugar) REFERENCES especies_marinas(id_especies_marinas) -- llave foranea con lugar

        );


        CREATE TABLE IF NOT EXISTS avistamientos(
            id_avistamientos INTEGER PRIMARY KEY,
            nombre_cientifico TEXT NO NULL,
            lugar TEXT NO NULL,
            latitud TEXT NO NULL,
            longitud TEXT NO NULL,
            autor TEXT NO NULL, 
            notas TEXT NO NULL,
            FOREIGN KEY (id_avistamientos) REFERENCES especies_marinas(id_especies_marinas) -- llave foranea con lugar

        );
-- ________________________________________________

CREATE TABLE IF NOT EXISTS categoria_taxonomica (
    id_taxonomica INTEGER PRIMARY KEY,
    reino TEXT NO NULL,
    filo TEXT NO NULL,
    clase TEXT NO NULL,
    orden TEXT NO NULL,
    familia TEXT NO NULL,
    genero TEXT NO NULL,
    especie TEXT NO NULL,
    FOREIGN KEY (id_taxonomica) REFERENCES especies_marinas(id_especies_marinas)
);

        CREATE TABLE IF NOT EXISTS especies (
            id_especie INTEGER PRIMARY KEY,
            nombre_comun TEXT NO NULL,
            nombre_cientifico TEXT NO NULL, -- tiene su llave foranea
            especie TEXT NO NULL,
            --FOREIGN KEY (especie) REFERENCES categoria_taxonomica(especie) -- llave foranea con lugar
            FOREIGN KEY (id_especie) REFERENCES categoria_taxonomica(id_taxonomica) -- llave foranea con lugar

        );
-- ______________________________________________________
