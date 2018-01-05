async function fetchAsync(url) {
    let response = await fetch(url);
    return await response.json();
}

let displayTweet = (data) => {
    document.querySelector("#tweetkov").style.display = "block";
    if (data.tweetkov == null) {
        document.querySelector("#tweetkov").innerHTML = "The selected Twitter user wasn´t found. Please try again";
        document.querySelector("#handle").focus();
        document.querySelector("#handle").value = "";
    } else {
        document.querySelector("#from").innerHTML = `<h2>Markovified <a href="https://twitter.com/${data.user}" target="_blank">@${data.user}</a>:</h2>`;
        document.querySelector("#tweet").innerHTML = `<h1>${data.tweetkov}</h1>`;
        document.querySelector("#shareButton").href = `https://twitter.com/intent/tweet?text=${data.tweetkov}&hashtags=tweetkov&url=${location.href}`
        document.querySelector("#spinner").style.display = "none";

    }

}

let tweetkovify = (user) => {
    fetchAsync(`../user/${user}`)
        .then(data => displayTweet(data))
};

document.querySelector("#generate").addEventListener("click", function () {
    document.querySelector("#spinner").style.display = "block";
    event.preventDefault();
    tweetkovify(document.querySelector("#handle").value);
})