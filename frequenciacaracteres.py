from collections import Counter

def analisa_frequencia_de_letras(texto):
    # Gera um dicionário de caracteres com o respectivo total de ocorrências desses caracteres
    aparicoes = Counter(texto.lower())

    # Totaliza todas as ocorrências obtidas no dicionário acima
    total_de_caracteres = sum(aparicoes.values())

    # Percorre os itens presentes no dicionário aparicoes extraindo, de cada item, o caracter e a frequência
    # de ocorrência daquele caracter. A partir dessa iteração, cria tuplas no formato caracter: percentual de
    # ocorrência.
    proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]

    # Atribui à variável proporcao um novo dicionário do tipo Counter usando as tuplas criadas na iteração
    # anterior.
    proporcoes = Counter(dict(proporcoes))

    # Gera uma lista contendo os 10 itens com maior frequência existentes no dicionário proporcoes.
    mais_comuns = proporcoes.most_common(10)

    # Percorre a lista gerada acima recuperando o caracter e sua proporção de ocorrência no texto.
    for caractere, proporcao in mais_comuns:
        # Imprime o caracter e seu percentual de ocorrência no texto.
        print("{} => {:.2f}%".format(caractere, proporcao * 100))


texto1 = """
Sergei Vasilyevich Rachmaninoff[a][b] (1 April [O.S. 20 March] 1873 – 28 March 1943) was a Russian composer, virtuoso pianist, and conductor. Rachmaninoff is widely considered one of the finest pianists of his day and, as a composer, one of the last great representatives of Romanticism in Russian classical music. Early influences of Tchaikovsky, Rimsky-Korsakov, and other Russian composers gave way to a thoroughly personal idiom notable for its song-like melodicism, expressiveness and rich orchestral colours.[4] The piano is featured prominently in Rachmaninoff's compositional output and he made a point of using his skills as a performer to fully explore the expressive and technical possibilities of the instrument.

Born into a musical family, Rachmaninoff took up the piano at the age of four. He studied with Anton Arensky and Sergei Taneyev at the Moscow Conservatory and graduated in 1892, having already composed several piano and orchestral pieces. In 1897, following the disastrous premiere of his Symphony No. 1, Rachmaninoff entered a four-year depression and composed little until successful supportive therapy allowed him to complete his enthusiastically received Piano Concerto No. 2 in 1901. In the course of the next sixteen years, Rachmaninoff conducted at the Bolshoi Theatre, relocated to Dresden, Germany, and toured the United States for the first time.

Following the Russian Revolution, Rachmaninoff and his family left Russia, and in 1918 they settled in New York City. With his primary source of income coming from performances as a pianist and a conductor, Rachmaninoff had little time to compose. Because of this, he completed just six works between 1918 and 1943, including the Rhapsody on a Theme of Paganini, Symphony No. 3, and Symphonic Dances. By 1942, his failing health led to his relocation to Beverly Hills, California, where he died the following year from advanced melanoma.
"""
print("Frequência no texto1")
analisa_frequencia_de_letras(texto1)

texto2 = """
The word "piano" is a shortened form of pianoforte, the Italian term for the early 1700s versions of the instrument, which in turn derives from clavicembalo col piano e forte (key cimbalom with quieter and louder)[1] and fortepiano. The Italian musical terms piano and forte indicate "soft" and "loud" respectively,[2] in this context referring to the variations in volume (i.e., loudness) produced in response to a pianist's touch or pressure on the keys: the greater the velocity of a key press, the greater the force of the hammer hitting the strings, and the louder the sound of the note produced and the stronger the attack. The name was created as a contrast to harpsichord, a musical instrument that does not allow variation in volume; compared to the harpsichord, the first fortepianos in the 1700s had a quieter sound and smaller dynamic range.[3]

A piano usually has a protective wooden case surrounding the soundboard and metal strings, which are strung under great tension on a heavy metal frame. Pressing one or more keys on the piano's keyboard causes a wooden or plastic hammer (typically padded with firm felt) to strike the strings. The hammer rebounds from the strings, and the strings continue to vibrate at their resonant frequency.[4] These vibrations are transmitted through a bridge to a soundboard that amplifies by more efficiently coupling the acoustic energy to the air. When the key is released, a damper stops the strings' vibration, ending the sound. Notes can be sustained, even when the keys are released by the fingers and thumbs, by the use of pedals at the base of the instrument. The sustain pedal enables pianists to play musical passages that would otherwise be impossible, such as sounding a 10-note chord in the lower register and then, while this chord is being continued with the sustain pedal, shifting both hands to the treble range to play a melody and arpeggios over the top of this sustained chord. Unlike the pipe organ and harpsichord, two major keyboard instruments widely used before the piano, the piano allows gradations of volume and tone according to how forcefully or softly a performer presses or strikes the keys.

Most modern pianos have a row of 88 black and white keys, 52 white keys for the notes of the C major scale (C, D, E, F, G, A and B) and 36 shorter black keys, which are raised above the white keys, and set further back on the keyboard. This means that the piano can play 88 different pitches (or "notes"), spanning a range of a bit over seven octaves. The black keys are for the "accidentals" (F♯/G♭, G♯/A♭, A♯/B♭, C♯/D♭, and D♯/E♭), which are needed to play in all twelve keys. More rarely, some pianos have additional keys (which require additional strings), an example of which is the Bösendorfer Concert Grand 290 Imperial, which has 97 keys.[5] Most notes have three strings, except for the bass, which graduates from one to two. The strings are sounded when keys are pressed or struck, and silenced by dampers when the hands are lifted from the keyboard. Although an acoustic piano has strings, it is usually classified as a percussion instrument rather than as a stringed instrument, because the strings are struck rather than plucked (as with a harpsichord or spinet); in the Hornbostel–Sachs system of instrument classification, pianos are considered chordophones. There are two main types of piano: the grand piano and the upright piano. The grand piano has a better sound and gives the player a more precise control of the keys, and is therefore the preferred choice for every situation in which the available floor-space and the budget will allow, as well as often being considered a requirement in venues where skilled pianists will frequently give public performances. The upright piano, which necessarily involves some compromise in both tone and key action compared to a grand piano of equivalent quality, is nevertheless much more widely used, because it occupies less space (allowing it to fit comfortably in a room where a grand piano would be too large) and is significantly less expensive.

During the 1800s, influenced by the musical trends of the Romantic music era, innovations such as the cast iron frame (which allowed much greater string tensions) and aliquot stringing gave grand pianos a more powerful sound, with a longer sustain and richer tone. In the nineteenth century, a family's piano played the same role that a radio or phonograph played in the twentieth century; when a nineteenth-century family wanted to hear a newly published musical piece or symphony, they could hear it by having a family member play a simplified version on the piano. During the nineteenth century, music publishers produced many types of musical works (symphonies, opera overtures, waltzes, etc.) in arrangements for piano, so that music lovers could play and hear the popular pieces of the day in their home. The piano is widely employed in classical, jazz, traditional and popular music for solo and ensemble performances, accompaniment, and for composing, songwriting and rehearsals. Although the piano is very heavy and thus not portable and is expensive (in comparison with other widely used accompaniment instruments, such as the acoustic guitar), its musical versatility (i.e., its wide pitch range, ability to play chords, louder or softer notes and two or more independent musical lines at the same time), the large number of musicians - both amateurs and professionals - trained in playing it, and its wide availability in performance venues, schools and rehearsal spaces have made it one of the Western world's most familiar musical instruments.
"""
print("\n\nFrequência no texto2")
analisa_frequencia_de_letras(texto2)
