    function calculateDebt(rate,time_in_years,total_med_school_cost){
    let p = total_med_school_cost / 4; // #yearly cost;
    let r = rate;
    let t = time_in_years;
    let a = [p*r**(t), p*r**(t-1), p*r**(t-2), p*r**(t-3)];
    let message = `
    Your total tuition will be <strong>$${total_med_school_cost}k</strong> over 4 years.<br>
    To pay this, you get 1 loan every year for $${p}k.<br>
    You get a <strong>${(100*(rate-1)).toFixed(2)}%</strong> interest rate and don't pay anything for <strong>${t} years</strong><br>
    By the time you start making payments, you will owe...<br>
    `;
    let sum_a = a[0] + a[1] + a[2] + a[3];
    let cost = `$${sum_a.toFixed(3)}k`;
    console.log(message)
    console.log(cost)
    return {message: message, cost:cost}
    }
    function updatePage(){

    let rate = document.getElementById('rate').value;
    let t = document.getElementById('t').value;
    let cost = document.getElementById('cost').value;

    if(!rate)rate = 1.06;
    if(!t)t = 8;
    if(!cost)cost = 244;
    let data = calculateDebt(rate, t, cost);
    document.getElementById('display_message').innerHTML = data.message;
    document.getElementById('display_cost').innerHTML = data.cost;
    }
    
