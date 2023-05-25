let datasheets = new Vue({
    el: '#api',
    delimiters: ['[[',']]'],
    data: {
        imperialKnightsUnitsList: [],
        imperialKnightsWargearList: [],
        armyList: [],
        pointTotal: 0,
        finalPointTotal: null,
        completedArmyList: null,
        listComplete: false,
    },
    methods: {
        getImperialKnightsUnits: function() {
            axios({
                method: 'GET',
                url: '/api/units/',
            }).then(res => this.imperialKnightsUnitsList = res.data)
        },

    },
    beforeMount: function() {
        this.getImperialKnightsUnits()
    }
});
