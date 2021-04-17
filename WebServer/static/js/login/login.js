/**
 *ログイン処理後
 * @param {*} data
 */
var afterFetch = function loginAfter(data) {
  alert("test");
  alert(data);
};

/**
 * ログインボタン押下
 */
function login() {
  param = {
    userId: $("#id")[0].value,
    password: $("#password")[0].value,
  };

  // ログイン処理
  commonLogin(param);
}
