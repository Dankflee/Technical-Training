function rotateLeft(a, d) {
    const n = a.length;
    d = d % n;
    if (d === 0) {
      return a;
    }
    for (let i = 0; i < d; i++) {
      const temp = a[0];
      for (let j = 1; j < n; j++) {
        a[j - 1] = a[j];
      }
      a[n - 1] = temp;
    }
    return a;
  }
  
  const arr = [1, 2, 3, 4, 5];
  const d = 2;
  const rotatedArr = rotateLeft(arr, d);
  console.log(rotatedArr);