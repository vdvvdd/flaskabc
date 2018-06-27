function add()
{
    var add1 = Number(document.form1.add1.value);
    var add2 = Number(document.form1.add2.value);
    var ret = add1 + add2;

    document.form1.result.value = ret;
}