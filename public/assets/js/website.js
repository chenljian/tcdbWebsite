/**
 * Created by tenghuanhe on 2016/7/15.
 */
$(function () {
    window.onload = function () {
        var oUl = document.getElementById("navigation");
        var oLi = oUl.getElementsByTagName("li");

        for (var i = 0; i < oLi.length; i++) {
            oLi[i].onmouseover = function () {
                this.className = "hover";
            };
            oLi[i].onmouseout = function () {
                this.className = "";
            };
        }
    }
});
