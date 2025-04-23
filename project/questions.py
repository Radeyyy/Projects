

questions_data = {
     "Biology": [
        {
                "question": "What gas do plants absorb from the atmosphere?",
                "choices": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
                "answer": "Carbon Dioxide"
        },
        {
                "question": "Which organ is primarily responsible for pumping blood?",
                "choices": ["Lungs", "Liver", "Heart", "Kidneys"],
                "answer": "Heart"
        },
        {
                "question": "What part of the cell contains genetic material?",
                "choices": ["Mitochondria", "Ribosome", "Nucleus", "Cytoplasm"],
                "answer": "Nucleus"
        },
        {
                "question": "What is the process by which plants make their food?",
                "choices": ["Respiration", "Transpiration", "Photosynthesis", "Digestion"],
                "answer": "Photosynthesis"
        },
        {
                "question": "Which macromolecule is responsible for carrying genetic information?",
                "choices": ["Carbohydrates", "Lipids", "Proteins", "Nucleic acids"],
                "answer": "Nucleic acids"
        }
    ],

    "Chemistry": [
        {
                "question": "What is the chemical symbol for water?",
                "choices": ["O2", "H2O", "CO2", "H2SO4"],
                "answer": "H2O"
        },
        {
                "question": "What is the boiling point of water in Celsius?",
                "choices": ["50°C", "75°C", "100°C", "120°C"],
                "answer": "100°C"
        },
        {
                "question": "Which of these is not a state of matter?",
                "choices": ["Solid", "Gas", "Liquid", "Energy"],
                "answer": "Energy"
        },
        {
                "question": "What kind of energy is stored in food?",
                "choices": ["Mechanical", "Chemical", "Thermal", "Sound"],
                "answer": "Chemical"
        },
        {
                "question": "What is the pH value of a neutral substance?",
                "choices": ["0", "7", "14", "1"],
                "answer": "7"
        }
    ],

    "Physics": [
        {
                "question": "Which planet is known as the Red Planet?",
                "choices": ["Earth", "Mars", "Jupiter", "Venus"],
                "answer": "Mars"
        },
        {
                "question": "What force pulls objects toward Earth?",
                "choices": ["Magnetism", "Friction", "Gravity", "Inertia"],
                "answer": "Gravity"
        },
        {
                "question": "What is the center of an atom called?",
                "choices": ["Proton", "Neutron", "Electron", "Nucleus"],
                "answer": "Nucleus"
        },
        {
                "question": "What instrument is used to measure temperature?",
                "choices": ["Thermostat", "Thermometer", "Barometer", "Altimeter"],
                "answer": "Thermometer"
        },
        {
                "question": "What unit is used to measure force?",
                "choices": ["Watt", "Joule", "Newton", "Volt"],
                "answer": "Newton"
        }
    ],

    "Earth Science": [
        {
                "question": "What is the molten rock beneath the Earth's surface called?",
                "choices": ["Lava", "Magma", "Basalt", "Granite"],
                "answer": "Magma"
        },
        {
                "question": "Which layer of the Earth is the hottest?",
                "choices": ["Crust", "Mantle", "Outer core", "Inner core"],
                "answer": "Inner core"
        },
        {
                "question": "What is the main cause of earthquakes?",
                "choices": ["Wind", "Tectonic plate movement", "Volcanic eruptions", "Gravity"],
                "answer": "Tectonic plate movement"
        },
        {
                "question": "Which gas is most abundant in the Earth's atmosphere?",
                "choices": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
                "answer": "Nitrogen"
        },
        {
                "question": "What type of rock is formed from molten lava?",
                "choices": ["Sedimentary", "Igneous", "Metamorphic", "Fossil"],
                "answer": "Igneous"
        }
    ]
}

# Get questions based on category
def get_questions(category):
    return questions_data.get(category, [])


