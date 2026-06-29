function ruleCheck(url) {
    let score= 0;
    if (url.length> 75) score++;
    if (url.includes("@")) score++;
    if ((url.match(/\./g) || []).length> 3) score++;
    if (/\d/.test(url)) score++;

    const susWords= ["login", "verify", "bank", "secure"];
    susWords.forEach(word=> {
        if (url.toLowerCase().includes(word)) score++;
    });
    return score;
}
module.exports = { ruleCheck };