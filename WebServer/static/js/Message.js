var MESSAGE_ARIA_ID = "messageAria";
/**
 * 画面にメッセージを表示させる
 * @param {出力するメッセージ(Object)} message
 */
function displayMessage(message) {
  // 現在表示されているメッセージをクリア
  clearDisplayMessage();

  // メッセージのチェック
  if (commonCheckIsNull(message)) {
    return;
  }

  // エラーメッセージあり
  if (!commonCheckIsNull(message.errMessage)) {
    displayErrorMessage();
  }

  // ノーマルメッセージあり
  if (!commonCheckIsNull(message.normalMessage)) {
  }
}

/**
 * メッセージエリアの文字列を書き換える
 */
function changeMessageAria(_html) {
  var message = $("div").attr("id", MESSAGE_ARIA_ID);
  message[0].innerHTML = _html;
}

/**
 * 画面のメッセージをクリア
 */
function clearDisplayMessage() {
  changeMessageAria("");
}

/**
 * 画面のメッセージをクリア
 */
function displayErrorMessage() {
  var htmlStr = "";
  htmlStr = htmlStr + "<ul class='alert alert-danger'>";
  htmlStr = htmlStr + "<li>" + "エラーメッセージ" + "</li>";
  htmlStr = htmlStr + "</ul>";

  changeMessageAria(htmlStr);
}
