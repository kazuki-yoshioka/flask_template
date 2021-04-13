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
    id: $("#id")[0].value,
    password: $("#password")[0].value,
  };

  commonFetchData(param, "fetch", null);
}
