/**
 * ログイン処理
 * @param {リクエストパラメータ} _param
 */
function commonLogin(_param) {
  if (!commonCheckFormatJson(_param)) {
    alert("パラメータがJson形式ではありません。");
    return;
  }
  var _url = "/Enter/Login/";

  // リクエストを送信
  sendRequestServer(_param, _url, null);
}
