const countdown = () => {
  const countDate = new Date("January 1, 2023 00:00:00").getTime();
  const now = new Date().getTime();
  const gap = countDate - now;

  // How does the time work?
  const second = 1000;
  const minute = second * 60;
  const hour = minute * 60;
  const day = hour * 24;

  // calculate
  const textDay = Math.floor(gap / day);
  const textHour = Math.floor((gap % day) / hour);
  const textMinute = Math.floor((gap % hour) / minute);
  const textSecond = Math.floor((gap % minute) / second);

  document.querySelector(".day").innerText = textDay;
  document.querySelector(".hour").innerText = textHour;
  document.querySelector(".minute").innerText = textMinute;
  document.querySelector(".second").innerText = textSecond;

  if (gap <= 0) {
    clearInterval(watchCountdown);
    document.querySelector(".day").innerHTML = "0";
    document.querySelector(".hour").innerHTML = "0";
    document.querySelector(".minute").innerHTML = "0";
    document.querySelector(".second").innerHTML = "0";
  }
};

let watchCountdown = setInterval(countdown, 1000);