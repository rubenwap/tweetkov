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
        document.querySelector("#shareButton").href = `https://twitter.com/intent/tweet?text=${data.tweetkov}&hashtags=tweetkov&url=${window.location}`
        document.querySelector(".spinner").style.display = "none";

    }

}

let tweetkovify = (user) => {
    fetchAsync(`../user/${user}`)
        .then(data => displayTweet(data)).catch(response => console.log(response))
};

document.querySelector("#generate").addEventListener("click", function () {
    event.preventDefault();
    ga('send', 'event', 'Click', 'Generate', 'Generate Tweetkovs');
    document.querySelector("#tweetkov").style.display = "none";
    document.querySelector(".spinner").style.display = "block";
    tweetkovify(document.querySelector("#handle").value);
})