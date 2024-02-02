function rev(arr){
    const revArr = [];
    for (let i = arr.length - 1 ; i>=0;i--){
        revArr.push(arr[i]);
    }
    return revArr;
}
const array = [1,4,3,2];
const revArr = rev(array);
console.log("Reversed Array is :- ",revArr)
