var app = new Vue({
    el:'#app',
    data:{
        name:null,
        age:null,
        sex:null,
    },
    methods:{
        onClick: function () {
            console.log('clicked');
        },
        onEnter: function () {
            console.log('mouse enter');
        },
        onOut: function () {
            console.log('mouse leave');
        },
        onSubmit: function () {
            // e.preventDefault();
            console.log('sumbitted');
        },
        onKeyup: function () {
            console.log('key pressed');
        }
    }
});