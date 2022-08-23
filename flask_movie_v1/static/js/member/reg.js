;//保证文件合并时不会出错
var member_reg_ops={

    init:function(){
        this.eventBind();
    },

    eventBind:function(){
        $(".reg_wrap .do-reg").click(function(){
            var login_name=$(".reg_wrap input[name=login_name]").val();
            var login_pwd1=$(".reg_wrap input[name=login_pwd1]").val();
            var login_pwd2=$(".reg_wrap input[name=login_pwd2]").val();
            if(login_name==undefined||login_name.length<1){
                alert("请输入正确的用户名~~");
                return;
            }
            if(login_pwd1==undefined||login_pwd1.length<6){
                alert("请输入正确的登录密码，并且不能小于6个字符~~");
                return;
            }
            if(login_pwd2==undefined||login_pwd2!=login_pwd1){
                alert("请输入正确的确认登录密码！");
                return;
            }
        });
    }
}
$(document).ready(function(){
    member_reg_ops.init();
});
