const {fork} = require("child_process");
count = 0;
for (let i=0 ;i<10;i++) {
    const child = fork("./child.js");
    child.on("close",(code)=>{
        count++;
        if(count == 10) {
            process.exit(0);
        }
    });
}