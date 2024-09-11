import streamlit as st
import base64

#Set Mode auf Wide
st.set_page_config(layout="wide")

# Logo einbetten
st.sidebar.image("Logo_of_Fachhochschule_Münster.png", use_column_width=True)
st.sidebar.image("Logo_FGV.png", use_column_width=True)

# Fixiert die Sidebar, so dass sie sich wie ein Header verhält
st.sidebar.markdown("""
    <style>
        .css-18e3th9 {  # Dies ist die Klasse für die Sidebar in Streamlit
            width: 50x;  # Breite der Sidebar anpassen
            position: fixed;
            right: 0;
            top: 0;
            height: 100%;
            margin-top: 0;
        }
        .css-1l02zno {  # Dies ist die Klasse für den Hauptcontainer
            margin-left: auto;
        }
    </style>
""", unsafe_allow_html=True)

# Custom CSS for changing the font size in an expander
st.markdown(
    """
    <style>
    .custom-expander .streamlit-expanderHeader {
        font-size: 20px; /* Change this value to the desired font size */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Titel und Beschreibung
st.title("Lange Nacht der Vertiefungen")
st.subheader("Vorstellung der Vertiefungsrichtung Verkehrswesen")

def show_pdf(file_path):
    # Datei einlesen und in Base64 umwandeln
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    
    # HTML und JavaScript, um die Breite dynamisch anzupassen
    pdf_html = f"""
    <iframe id="pdfEmbed" src="data:application/pdf;base64,{base64_pdf}" style="width:100%; height:100vh;" frameborder="0"></iframe>
    <script>
    window.onload = function() {{
        let pdfEmbed = document.getElementById('pdfEmbed');
        pdfEmbed.style.height = document.documentElement.clientHeight + 'px';
    }};
    </script>
    """
    
    # Ausgabe im Streamlit Dashboard
    st.markdown(pdf_html, unsafe_allow_html=True)


st.markdown("### Studium und Lehre")

with st.expander("Modulplan 3. - 6. Semester"):
        file_path1 = 'Modulplan 3. - 6. Semester.pdf'
        show_pdf(file_path1)

with st.expander("Fachgebiete"):

    tab_1, tab_2 , tab_3, tab_4, tab_5, tab_19 = st.tabs(["StraßenentwurfVerkehrstechnik", "Straßenbautechnik", "Planungsprogramme", "Praxisbezug","Schienenverkehrsbau", "Verkehrssimulation"])

    # Tab für Straßenentwurf und Verkehrstechnik
    with tab_1:
        st.header("Straßenentwurf und Verkehrstechnik")
        file_path3 = 'Plakate Fachgebiete_A0Teil1_StraßenentwurfVerkehrstechnik.pdf'
        show_pdf(file_path3)

    # Tab für Straßenbautechnik
    with tab_2:
        st.header("Straßenbautechnik")
        file_path4 = 'Plakate Fachgebiete_A0Teil2_Straßenbautechnik.pdf'
        show_pdf(file_path4)

    # Tab für Planungsprogramme
    with tab_3:
        st.header("Planungsprogramme")
        file_path5 = 'Plakate Fachgebiete_A0Teil3_Planungsprogramme.pdf'
        show_pdf(file_path5)

    # Tab für Praxisbezug
    with tab_4:
        st.header("Praxisbezug")
        file_path6 = 'Plakate Fachgebiete_A0Teil4_Praxisbezug.pdf'
        show_pdf(file_path6)

    # Tab für Schienenverkehrsbau
    with tab_5:
        st.header("Schienenverkehrsbau")
        file_path7 = 'Plakate Fachgebiete_A0Teil5_Schienenverkehrsbau.pdf'
        show_pdf(file_path7)

    with tab_19:
        st.header("Verkehrssimulation")
        # URL zur Videodatei
        video_url = 'lange-nacht-der-vertiefungsrichtungen_klein.mp4'
        # Video in Streamlit einbinden
        st.video(video_url)
        st.info("Quelle: FH Münster, Thomas Schönauer im Master-Modul Makro- und Mikroskopische Verkehrsmodellierung (26.02.2020)")

with st.expander("Projekte des Verkehrswesens I (4. Semester)"):

    st.write("""
             Im Modul "Projekte des Verkehrswesens" I im 4. Semester wird ein Projekt in Kleingruppen selbständig geplant, bearbeitet und präsentiert. 
             Die Themen variieren jährlich und greifen aktuelle Fragestellungen aus den Bereichen der Planung, des Entwurfs oder des
            Straßenbaus auf.""")
    tab_10, tab_11, tab_12, tab_13 = st.tabs(["2024 - Evaluation von Fahrradstraßen", "2023 - Radverkehrssicherheit in Münster", "2022 - Stadtmobilität Iserlohn", "2021 - Erhaltungsentwurf A52"])

    with tab_10:
        st.header("2024 - Evaluation von Fahrradstraßen")
        st.write("""
                In den letzten Jahren wurden viele Straßen als Fahrradstraßen ausgewiesen. 
                Allerdings gibt es dazu noch keine bundesweiten Ausgestaltungshinweise, inwiefern sich diese von anderen Straßen unterscheiden sollen.  
                Aus diesem Grund hat die Stadt Münster einen eignen Standard eingeführt und eines der Hauptmerkmale ist die flächige rot Markierung. 
                Durch die rote Markierung kann es zu einer Veränderung der Oberflächenstruktur kommen. 
                Die Aufgabe in diesem Jahr umfasst eine Erstellung von Bewertungskriterien, sowie die Festlegung von Messverfahren zur Erfassung von Zustandswerten. 
                Gleichzeitig sollen eigene Ideen, Konzepte und Lösungsansätze formulieren werden. 
                """)
        
        col1, col2 = st.columns(2)
        #Ergänze Bilder
        with col1:
            st.image("VP1_1.1.png", use_column_width=True)
            st.info("Quelle: Stadt Münster")
        with col2:
            st.image("VP1_1.3.png", use_column_width=True)
            st.info("Quelle: Stadt Münster, Bismarckstraße in Münster")

    with tab_11:
        st.header("2023 - Radverkehrssicherheit in Münster")
        st.write("""
                Der Radverkehr ist ein wesentlicher Punkt für die Umsetzung der Verkehrswende; 
                um diesen auch weiterhin zu stärken, müssen die Radverkehrsanlagen in einem guten Zustand und sicher sein. 
                Die Projektaufgabe war es, einen Kriterienkatalog zu erstellen, welcher quantitative und qualitative Aspekte wie Oberflächenzustand, Sichtbarkeit von Markierungen, Sicherheit von Kreuzungen und Barrierefreiheit berücksichtigt. 
                Anschließend wird der aktuelle Zustand des Radweges analysiert und Verbesserungsvorschläge erarbeitet, welche die Kriterien aus dem Katalog erfüllen, um die Radwege langfristig attraktiver zu gestalten.
                """)
        col1, col2 = st.columns(2)
        with col1:        #Ergänze Bilder
            st.image("Radverkehrssicherheit.png", use_column_width=True)
            st.info("Quelle: Stadt Münster, Derek Pommer")
        with col2:
            st.image("Bild_Unfall.png", use_column_width=True)
            st.info("Quelle: Westfälische Nachrichten (01.06.2023)")
        st.markdown(
        """
        <iframe src="https://unfallatlas.statistikportal.de/" width="100%" height="600px"></iframe>
        """,
        unsafe_allow_html=True)
        st.info("Quelle: Statistische Ämter des Bundes und der Länder (2024): Unfallatlas")

    with tab_12:
        st.header("2022 - Stadtmobilität Iserlohn")
        st.write("""
                Das Projekt wurde zusammen mit der Stadt Iserlohn erstellt. 
                Es handelt sich hierbei um eine konzeptionelle Planung, um den Nahverkehr sowie Rad- und Fußgängerverkehr zu stärken und besser auszubauen.
                Die Aufgabe war es die Anbindung vom Waldstadt-Quartier zum Stadtbahnhof unter Berücksichtigung der aktiven Mobilität zu untersuchen und die Möglichkeit von weiteren Haltestellen in Betracht zu ziehen. 
                Weiterhin wollte die Stadt Iserlohn ein Folgeprojekt für den a-Bus etablieren. 
                Dafür sollen eigene Ideen für einen Streckenführungen eingebracht werden. Ziel dieses Projektes ist die nachhaltige Quartiersentwicklung rund um den Stadtbahnhof weiterentwickeln.
                """)
        #Ergänze Bilder
        col1, col2 = st.columns(2)
        with col1:
            st.image("VP1_3.1.png", use_column_width=True)
            st.info("Quelle: Stadt Iserlohn (2022): Smart City in Iserlohn, aBus Iserlohn")
        with col2:
            st.image("VP1_3.2.png", use_column_width=True)
            st.info("Quelle: Wikipedia - Datei: Autonomer Bus Easymile Iserlohn.jpg")

    with tab_13:
        st.header("2021 - Erhaltungsentwurf A52")
        st.write("""
                Dieses Projekt ist eine Zusammenarbeit mit der Autobahn AG. 
                Es wird eine Maßnahme für den Erhalt für den Streckenzug BAB 52 gefordert. 
                Die Aufgabe in dem Jahr 2021 war es, ein Erhaltungskonzept zu erstellen, mit einer einheitlichen Analyse der bestehenden Straßenabschnitte. 
                Anschließend sollte ein Erhaltungsentwurf für den Streckenzug erstellt werden, der die Randbedingungen beim Bauen im Bestand berücksichtigt. 
                Der Entwurf sollte für eine Nutzungsdauer von 30 Jahren ausgelegt sein und die Art der Fahrbahnbefestigung mit einbeziehen. 
                Zudem war die Verkehrsführung während des Umbaus zu betrachten, ebenso wie die voraussichtliche Bauzeit und Kosten.
                """)
        #Ergänze Bilder
        col1, col2 = st.columns(2)
        with col1:
            st.image("VP1_4.1.png", use_column_width=True)
            st.info("Quelle: FH Münster (2021): Erhaltungsentwurf A52")
        with col2:
            st.image("VP1_4.2.png", use_column_width=True)
            st.info("Quelle: Autobahn AG (2021)")

with st.expander("Exkursionen"):
    st.markdown("Seit 2007 sind mehr als 50 Exkursionen durchgeführt worden!")
    tab_14, tab_15, tab_16, tab_17, tab_18 = st.tabs(["2023 - Großbaustelle B51 – B481 Umgehungsstraße Münster", "2023 - Ruhrgebiet, Niederlande, Münsterland", "2022 - Asphaltmischanlage Oberhausen / BAB A31 ", "2022 - Stuttgart, Frankfurt, Würzburg, Leverkusen", "2022 - Intertraffic Amsterdam "]) 

    with tab_14:
        st.header("2023 - Großbaustelle B51 – B481 Umgehungsstraße Münster")
        st.image("Exkursion_1.png", use_column_width=True)

    with tab_15:
        st.header("2023 - Ruhrgebiet, Niederlande, Münsterland")
        st.image("Exkursion_2.png", use_column_width=True)

    with tab_16:
        st.header("2022 - Asphaltmischanlage Oberhausen / BAB A31")
        st.image("Exkursion_3.png", use_column_width=True)

    with tab_17:
        st.header("2022 - Stuttgart, Frankfurt, Würzburg, Leverkusen")
        st.image("Exkursion_4.png", use_column_width=True)

    with tab_18:
        st.header("Intertraffic Amsterdam 2022")
        st.image("Exkursion_5.png", use_column_width=True)

with st.expander("Potenzielle Arbeitgeber"):
    file_path2 = 'Potenzielle Arbeitgeber.pdf'
    show_pdf(file_path2)


st.markdown("### Die Forschungsgruppe Verkehrswesen")

with st.expander("Das Team"):
    tab_1, tab_2 = st.tabs(["Das Team", "Professoren"])
    
    with tab_1:
        #Erstelle 2 Spalten
        st.subheader("Das Team:")
        st.write("""Das Team v.l.n.r.: Adrian Gumz, Jonas Wenkers, Tom Mellmann, Peter Bruder, Janik Schründer (ehemalig), Thomas Schönauer, Jeanette Klemmer, Robin Kersten, Hans-Hermann Weßelborg, Hendrik Ebbers und Birgit Hartz""")
        # Bildpfad
        image_path = "Team.jpg"

        # CSS zum Zentrieren des Bildes
        st.markdown(
            f"""
            <style>
            .center {{
                display: block;
                margin-left: auto;
                margin-right: auto;
            }}
            </style>
            <img src="data:image/jpg;base64,{base64.b64encode(open(image_path, "rb").read()).decode()}" class="center" width="1000">
            """,
            unsafe_allow_html=True,
        )
        st.info("Foto: Anna Haas")

    with tab_2:
        st.subheader("Professoren:")
        #Erstelle 3 Spalten
        col1, col2, col3 = st.columns(3)
        #Füge Professoren hinzu
        col1.image("Weßelborg.jpg", use_column_width=True)
        col1.write("<p align='center'><b> Prof. Dr.-Ing. H.-H. Weßelborg</b></p>", unsafe_allow_html=True)
        col1.write("<p align='center'>Prof. an der FH Münster seit Oktober 2006</p>", unsafe_allow_html=True)
        col1.write("<p align='center'>Forschungsschwerpunkte: Straßenbautechnik, Straßenbetrieb, Straßenerhaltung</p>", unsafe_allow_html=True)
        
        col2.image("Hartz.jpg", use_column_width=True)
        col2.write("<p align='center'><b> Prof. Dr.-Ing. B. Hartz</b></p>", unsafe_allow_html=True)
        col2.write("<p align='center'>Prof. an der FH Münster seit März 2012</p>", unsafe_allow_html=True)
        col2.write("<p align='center'>Forschungsschwerpunkte: Verkehrstechnik, Verkehrsplanung, Verkehrssicherheit, Verkehr und Umwelt</p>", unsafe_allow_html=True)
        
        col3.image("Klemmer.jpg", use_column_width=True)
        col3.write("<p align='center'><b> Prof. Dr.-Ing. J. Klemmer</b></p>", unsafe_allow_html=True)
        col3.write("<p align='center'>Prof. an der FH Münster seit März 2019</p>", unsafe_allow_html=True)
        col3.write("<p align='center'>Forschungsschwerpunkte: Konzeptionelle Verkehrsplanung, Straßenentwurf, Schienenverkehrswesen, nachhaltige Mobilität</p>", unsafe_allow_html=True)


with st.expander("Forschungsaktivitäten"):
    tab_6, tab_7 , tab_8, tab_9, tab_10, tab_11= st.tabs(["Wissenschaftliche Begleitforschung LOOPmünster", "REKOTI - Ressourcenplan kommunaler Tiefbau", "Durchführung von PID-Messungen beim Einbau von Walzasphalt", "Verkehrsversuch Rathausstraße - Greven", "Detaillierte Untersuchung der Radverkehrsunfälle in der Stadt Münster", "Intelligente Beleuchtung an Münsters Kanalpromenade"])
    with tab_6:
        st.subheader("Wissenschaftliche Begleitforschung LOOPmünster")
        st.write(""" Die wissenschaftliche Begleitstudie der FH Münster hat das vierjährige Pilotprojekt LOOPmünster, ein On-Demand-Ridepooling-System, eingehend analysiert. 
        Seit seiner Einführung im September 2020 im Süden Münsters bietet dieser flexible öffentliche Nahverkehrsdienst eine fahrplanunabhängige Mobilitätslösung, die Fahrten auf Bestellung bündelt und koordiniert. 
        Die Studie, geleitet von Prof. Dr. Jeanette Klemmer, zeigt, dass LOOPmünster sich als wertvolle Ergänzung zum bestehenden Verkehrsnetz etabliert hat und wichtige Impulse für die Mobilitätswende liefert.
        Die Forschungsgruppe hat durch Umfragen und die Analyse von Betriebs- sowie Strukturdaten tiefgreifende Einblicke gewonnen und basierend darauf Empfehlungen für die Weiterentwicklung des Services gegeben. 
        Anpassungen im Betriebsgebiet und bei der Dienstverfügbarkeit wurden aufgrund der Rückmeldungen von Nutzenden und Fahrpersonal vorgenommen, was zu einer gesteigerten Kundenzufriedenheit führte. 
        Die Ergebnisse der Studie unterstreichen die positive Resonanz auf den Dienst und dienen als Basis für zukünftige Entscheidungen zur nachhaltigen Gestaltung des ÖPNV in Münster.""")
        # Bildpfad
        image_path2 = "Bild_LOOP.jpg"
        # CSS zum Zentrieren des Bildes
        st.markdown(
            f"""
            <style>
            .center {{
                display: block;
                margin-left: auto;
                margin-right: auto;
            }}
            </style>
            <img src="data:image/jpg;base64,{base64.b64encode(open(image_path2, "rb").read()).decode()}" class="center" width="1000">
            """,
            unsafe_allow_html=True,
        )
        st.info("Quelle: Stadtwerke Münster GmbH")

    with tab_7:
        st.subheader("REKOTI - Ressourcenplan kommunaler Tiefbau")
        st.write('''
        Ein Beitrag zur Nachhaltigkeit im Asphaltstraßenbau, durch eine hochwertige Wiederverwendung von Asphalt und dem Einsatz von Niedrigtemperaturasphalt.
        Das vom Bundesministerium für Bildung und Forschung geförderte Forschungsprojekt „RekoTi – Ressourcenplan kommunaler Tiefbau“ (Förderkennzeichen: 033R264) befasst sich mit der Steigerung der Ressourceneffizienz im kommunalen Tiefbau. 
        Betrachtet werden hierbei die Infrastrukturanlagen Verkehrsflächen, Brücken und Kanalisation, für welche ein mit BIM-Technologien unterstützter Ressourcenplan erstellt wird. 
        Im Bereich der Verkehrsflächen erfolgte dabei der Bau einer Versuchsstrecke, bei welcher Ende 2022 sechs Versuchsfelder mit unterschiedlichen Asphaltgranulatanteilen unter dem Einsatz von Niedrigtemperaturasphalt und konventionell heißgemischtem Asphalt in einer Splittmastixasphalt-Deckschicht (SMA 8 S) realisiert wurden.
        ''')
        # YouTube-Video-URL
        video_url = 'https://www.youtube.com/embed/F5JMnhSPJ60?si=fRoBiPLbPCAg6wHY'  # Verwenden Sie den "embed"-Link für HTML
        # HTML-Code zum Einbetten des YouTube-Videos mit benutzerdefinierter Größe
        video_html = f"""
            <div style="display: flex; justify-content: center;">
                <iframe width="1000" height="450" src="{video_url}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            </div>
        """
        # HTML in Streamlit anzeigen
        st.markdown(video_html, unsafe_allow_html=True)

    with tab_8:
        st.subheader("Durchführung von PID-Messungen (Photoionisationsdetektor) beim Einbau von Walzasphalt")
        st.write('''
        Durch den Einsatz von TA-Asphalt und Absaugeinrichtungen an der Fertigerbohle kann der ab Ende 2024 geltende Arbeitsplatzgrenzwert (AGW) bisher nicht prozesssicher eingehalten werden. 
        Einflussfaktoren denen in der Vergangenheit eine teils geringere Bedeutung zugeschrieben wurde, rücken daher in den Vordergrund. 
        Anhand von ergänzenden Emissionsmessungen mit Photoionisationsdetektoren (PID) sowie durch Laboruntersuchungen wurden daher mögliche Einflussfaktoren ermittelt und bewertet.''')
        # Bildpfad
        image_path3 = "PID.png"
        # CSS zum Zentrieren des Bildes
        st.markdown(
            f"""
            <style>
            .center {{
                display: block;
                margin-left: auto;
                margin-right: auto;
            }}
            </style>
            <img src="data:image/jpg;base64,{base64.b64encode(open(image_path3, "rb").read()).decode()}" class="center" width="1000">
            """,
            unsafe_allow_html=True)
        st.info("Quelle: FH Münster, Thomas Schönauer")

    with tab_9:
        st.subheader("Verkehrsversuch Rathausstraße - Greven")
        st.write('''
        In der wissenschaftlichen Begleitforschung zum Projekt „Umgestaltung der Rathausstraße in Greven“ wird untersucht, wie die Neugestaltung dieser zentralen Verkehrsachse die Mobilitätsbedingungen für Fußgänger und Radfahrer verbessern kann. 
        Die Rathausstraße, eine Hauptverkehrsstraße mit einer täglichen Belastung von ca. 11.000 Kfz, ist seit 2014 in der Baulast der Stadt und spielt eine entscheidende Rolle im städtischen Verkehrskonzept. 
        Ziel der Umgestaltung ist es, die Attraktivität der Straße für nicht-motorisierte Verkehrsteilnehmer zu erhöhen und ihre trennende Wirkung auf umliegende Fußgängerzonen zu mindern. 
        Die Forschung soll evidenzbasierte Empfehlungen liefern, um eine effektive und akzeptierte Neugestaltung der Rathausstraße zu ermöglichen, die die Bedürfnisse aller Verkehrsteilnehmer berücksichtigt.
        ''')
        # Bildpfad
        image_path4 = "VVGreven.png"
        # CSS zum Zentrieren des Bildes
        st.markdown(
            f"""
            <style>
            .center {{
                display: block;
                margin-left: auto;
                margin-right: auto;
            }}
            </style>
            <img src="data:image/jpg;base64,{base64.b64encode(open(image_path4, "rb").read()).decode()}" class="center" width="1000">
            """,
            unsafe_allow_html=True)
        st.info("Quelle: Münstersche Zeitung: Autos raus per Einbahnstraße (15.04.22)")

    with tab_10:
        st.subheader("Detaillierte Untersuchung der Radverkehrsunfälle in der Stadt Münster")
        st.write("""Die von der Ordnungspartnerschaft Verkehrsunfallprävention Münster in Auftrag gegebene Untersuchung der Radverkehrsunfälle aus dem Jahr 2019 in Münster dient der Förderung der Verkehrssicherheit von Radfahrenden. 
                 Sie formuliert Maßnahmen für die Reduzierung von Radverkehrsunfällen sowie den Umgang mit vorliegenden Unfalldaten. 
                 Dabei liegt der Fokus auf Radverkehrsunfälle, welche nicht durch die Unfallkommission (Uko) an Unfallhäufungsstellen (UHS) und -linien (UHL) der Einjahreskarte betrachtet und analysiert werden.""")
        # Bildpfad
        image_path5 = "Radverkehrssicherheit.png"
        # CSS zum Zentrieren des Bildes
        st.markdown(
            f"""
            <style>
            .center {{
                display: block;
                margin-left: auto;
                margin-right: auto;
            }}
            </style>
            <img src="data:image/jpg;base64,{base64.b64encode(open(image_path5, "rb").read()).decode()}" class="center" width="1000">
            """,
            unsafe_allow_html=True)
        st.info("Quelle: Stadt Münster, Derek Pommer")
        
    with tab_11:
        st.subheader("Intelligente Beleuchtung an Münsters Kanalpromenade")
        st.write('''
        Die Kanalpromenade soll für Fahrradfahrende komfortabler und sicherer werden. Auf einer Teststrecke hat die Stadt Münster in Zusammenarbeit mit den Stadtwerken Münster hierfür bereits eine sogenannte intelligente Beleuchtung installiert. 
        Um erste Einschätzungen der Nutzerinnen und Nutzer zu erfragen, führte das Amt für Mobilität und Tiefbau mit wissenschaftlicher Unterstützung der FH Münster vor Ort und online eine Befragung durch. 570 Personen folgten dem Aufruf der Stadt Münster und nahmen an der Umfrage teil.
        Ziel war es, die Meinung der Nutzenden in Erfahrung zu bringen und die gewonnenen Erkenntnisse in die Umsetzung vor Ort sowie in weitere Planungen einzubeziehen.
        ''')
        # Bildpfad
        image_path6 = "IntelligenteBeleuchtung.jpg"
        # CSS zum Zentrieren des Bildes
        st.markdown(
            f"""
            <style>
            .center {{
                display: block;
                margin-left: auto;
                margin-right: auto;
            }}
            </style>
            <img src="data:image/jpg;base64,{base64.b64encode(open(image_path6, "rb").read()).decode()}" class="center" width="1000">
            """,
            unsafe_allow_html=True)
        st.info("Quelle: Stadt Münster, Smartcity Münster")

st.markdown("### Quiz")

with st.expander("Quiz"):
    st.write("Teste dein Wissen über Verkehrsplanung! Beantworte die folgenden Fragen. Jede Frage ist mit einem Punkt bewertet.")
    st.write("Viel Erfolg!")
    def main():
        st.title("Quiz zum Verkehrswesen")

        questions = [
            ("Was ist das Hauptziel von Verkehrsberuhigungsmaßnahmen in städtischen Gebieten?",
            ["Die Geschwindigkeit des Verkehrs zu erhöhen", "Mehr Parkplätze zu schaffen", "Die Sicherheit und Lebensqualität zu verbessern", "Öffentliche Verkehrsmittel abzuschaffen"],
            "Die Sicherheit und Lebensqualität zu verbessern"),
            ("Welche Technologie wird zunehmend in intelligenten Verkehrssystemen (ITS) verwendet, um den Verkehrsfluss zu optimieren?",
            ["Künstliche Intelligenz", "Dampfmaschinen", "Manuelle Verkehrszählung", "Morsecode"],
            "Künstliche Intelligenz"),
            ("Warum ist die Planung von Fußgängerzonen in Städten wichtig?",
            ["Um den Verkauf von Fahrzeugen zu fördern", "Um öffentliche Räume zugänglicher und sicherer zu machen", "Um den Bau von Hochhäusern zu verhindern", "Um den Kraftstoffverbrauch zu erhöhen"],
            "Um öffentliche Räume zugänglicher und sicherer zu machen"),
            ("Was versteht man unter 'Verkehrsmodellierung'?",
            ["Ein neues Model für Fahrzeuge entwerfen", "Die Analyse und Simulation von Verkehrsflüssen", "Die Herstellung von Miniaturfahrzeugen", "Die Erstellung von Modekatalogen für Autofahrende"],
            "Die Analyse und Simulation von Verkehrsflüssen"),
            ("Welche Rolle spielt die Nachhaltigkeit in der modernen Verkehrsplanung?",
            ["Sie wird ignoriert, da sie zu teuer ist", "Sie ist zentral, um langfristig lebenswerte Städte zu schaffen", "Sie betrifft nur den Bau von Straßen", "Sie ist nur ein Marketingbegriff"],
            "Sie ist zentral, um langfristig lebenswerte Städte zu schaffen")
        ]

        answers = {}
        for i, (question, options, correct_answer) in enumerate(questions, start=1):
            st.subheader(f"Frage {i}")
            st.write(question)
            answers[i] = st.radio("Wähle eine Antwort:", options, key=f"q{i}")

        if st.button("Alle Antworten überprüfen"):
            score = sum(1 for i, (_, _, correct_answer) in enumerate(questions, start=1) if answers[i] == correct_answer)
            st.subheader("Ergebnis")
            st.write(f"Du hast {score} von {len(questions)} Fragen richtig beantwortet!")
            # Optional: detailliertes Feedback anzeigen
            for i, (_, _, correct_answer) in enumerate(questions, start=1):
                if answers[i] == correct_answer:
                    st.success(f"Frage {i}: Richtig!")
                else:
                    st.error(f"Frage {i}: Falsch! Die richtige Antwort ist: {correct_answer}")

        if st.button("Umfrage zurücksetzen"):
            for i in range(1, len(questions) + 1):
                st.session_state.pop(f"q{i}", None)
            st.experimental_rerun()

    if __name__ == "__main__":
        main()
                


