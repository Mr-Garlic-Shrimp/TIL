var obj = {
    a: 1,
    b: 2,
    sum: function () {
        return this.a + this.b;
    }
};
console.log(obj.sum());
