TEST_USERS = {
    "ACTIVE": {
        'type': 'standard',
        'userName': 'regressiona',
        'password': 'epic1234',
        'firstName': 'A',
        'lastName': 'Regression',
        'surgeryTitle': 'Knee Arthroscopy & Recovery',
        'surgeryDate': 'nn'
    },

    "PRE_OP_NOT_SCHEDULED": {
        'type': 'standard',
        'userName': 'automation9',
        'password': 'epic1234',
        'firstName': 'Nine',
        'lastName': 'Automation',
        'surgeryTitle': 'Total Knee Replacement & Recovery',
        'surgeryDate': '19/12/2024'
    },

    "PRE_OP_ONE_CASE": {
        'type': 'standard',
        'userName': 'automation1',
        'password': 'epic1234',
        'firstName': 'One',
        'lastName': 'Automation',
        'surgeryTitle': 'Total Knee Replacement & Recovery',
        'surgeryDate': '09/04/2024'
    },

    "PRE_OP_TWO_CASES": {
        'type': 'standard',
        'userName': 'automation10',
        'password': 'epic1234',
        'firstName': 'Ten',
        'lastName': 'Automation',
        'surgeryTitle': 'Rotator Cuff Repair & Recovery',
        'surgeryDate': '13/12/2024'
    },

    "TEST_OP_ONE_CASE": {
        'type': 'standard',
        'userName': 'automation1',
        'password': 'epic1234',
        'firstName': 'Twelve',
        'lastName': 'Automation',
        'surgeryTitle': 'Total Knee Replacement & Recovery',
        'surgeryDate': '30/12/2024',
        'tasks': {
            'PSS': {
                'title': 'Watch: Advance Directives',
                'cta': 'Play video',
            }
        },
    },
    "PRE_OP_PSS_NOT_SCHEDULED": {
        'type': 'standard',
        'userName': 'automation12',
        'password': 'epic1234',
        'firstName': 'Twelve',
        'lastName': 'Automation',
        'surgeryTitle': 'Total Knee Replacement & Recovery',
        'surgeryDate': '30/12/2024',
        'tasks': {
            'PSS': {
                'title': 'Call 212.774.2305 to schedule your Pre-Surgical Screening Day',
                'cta': 'View details',
            }
        },
    },

    "PRE_OP_PSS_SCHEDULED": {
        'type': 'standard',
        'userName': 'automation13',
        'password': 'epic1234',
        'firstName': 'Thirteen',
        'lastName': 'Automation',
        'surgeryTitle': 'Total Hip Replacement & Recovery',
        'surgeryDate': '31/12/2024',
        'tasks': {
            'Itinerary': {
                'title': 'Review your 7/10/2024 pre-surgical appointments',
                'cta': 'View itinerary',
            }
        },
    },

    "AT_THE_HOSPITAL": {
        'type': 'standard',
        'userName': 'automation2',
        'password': 'epic1234',
        'firstName': 'Two',
        'lastName': 'Automation',
        'surgeryTitle': 'Rotator Cuff Repair & Recovery',
        'surgeryDate': '11/12/2023'
    },

    "AT_THE_HOSPITAL_BEDSIDE": {
        'type': 'bedside',
        'userName': 'annatest',
        'password': 'epic1234',
        'firstName': 'Test',
        'lastName': 'Anna',
        'surgeryTitle': 'Total Hip Replacement & Recovery',
        'surgeryDate': '30/12/2023'
    },

    "POST_OP_ACTIVE": {
        'type': 'standard',
        'userName': 'automation3',
        'password': 'epic1234',
        'firstName': 'Three',
        'lastName': 'Automation',
        'surgeryTitle': 'Total Knee Replacement & Recovery',
        'surgeryDate': '01/02/2024'
    },

    "LIMITED_USER": {
        'type': 'limited',
        'userName': 'automation7',
        'password': 'epic1234',
        'firstName': 'Three',
        'lastName': 'Automation',
        'surgeryTitle': 'Total Knee Replacement & Recovery',
        'surgeryDate': '01/02/2024'
    },
}
