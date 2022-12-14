const canvas = document.getElementById('canvas1');
const contxt = canvas.getContext('2d');
canvas.width = 900;
canvas.height = 600;

// global variables
const cellSize = 100;
const cellGap = 3;
let numberOfResources = 300;
let enemiesInterval = 600;
let frame = 0;
let gameOver = false;
let score = 0;
const winningScore = 50;
let choosenDefender = 1;

const gameGrid = [];
const defenders = [];
const enemies = [];
const enemyPositions = [];
const projectiles = [];
const resources = [];

// mouse
const mouse = {
    x: 10,
    y: 10,
    width: 0.1,
    height: 0.1,
    clicked: false
}
canvas.addEventListener('mousedown', function(){
    mouse.clicked = true;
});
canvas.addEventListener('mouseup', function(){
    mouse.clicked = false;
});
let canvasPosition = canvas.getBoundingClientRect();
canvas.addEventListener('mousemove', function(e){
    mouse.x = e.x - canvasPosition.left;
    mouse.y = e.y - canvasPosition.top;
});
canvas.addEventListener('mouseleave', function(){
    mouse.y = undefined;
    mouse.y = undefined;
});

// game board
const controlsBar = {
    width: canvas.width,
    height: cellSize,
}
class Cell {
    constructor(x, y){
        this.x = x;
        this.y = y;
        this.width = cellSize;
        this.height = cellSize;
    }
    draw(){
        if (mouse.x && mouse.y && collision(this, mouse)){
            contxt.strokeStyle = 'black';
            contxt.strokeRect(this.x, this.y, this.width, this.height);
        }
    }
}
function createGrid(){
    for (let y = cellSize; y < canvas.height; y += cellSize){
        for (let x = 0; x < canvas.width; x += cellSize){
            gameGrid.push(new Cell(x, y));
        }
    }
}
createGrid();
function handleGameGrid(){
    for (let i = 0; i < gameGrid.length; i++){
        gameGrid[i].draw();
    }
}
// projectiles
class Projectile {
    constructor(x, y){
        this.x = x;
        this.y = y;
        this.width = 10;
        this.height = 10;
        this.power = 20;
        this.speed = 10;
    }
    update(){
        this.x += this.speed;
    }
    draw(){
        contxt.fillStyle = 'orange';
        contxt.beginPath();
        contxt.arc(this.x, this.y, this.width, 0, Math.PI * 2);
        contxt.fill();
    }
}
function handleProjectiles(){
    for (let i = 0; i < projectiles.length; i++){
        projectiles[i].update();
        projectiles[i].draw();

        for (let j = 0; j < enemies.length; j++){
            if (enemies[j] && projectiles[i] && collision(projectiles[i], enemies[j])){
                enemies[j].health -= projectiles[i].power;
                projectiles.splice(i, 1);
                i--;
            }
        }

        if (projectiles[i] && projectiles[i].x > canvas.width - cellSize){
            projectiles.splice(i, 1);
            i--;
        }
    }
}

// defenders
const defender1 = new Image();
defender1.src = 'defender1.png';
const defender2 = new Image();
defender2.src = 'defender2.png';

class Defender {
    constructor(x, y){
        this.x = x;
        this.y = y;
        this.width = cellSize - cellGap * 2;
        this.height = cellSize - cellGap * 2;
        this.shooting = false;
        this.shootNow = false;
        this.health = 100;
        this.projectiles = [];
        this.timer = 0;
        this.frameX = 0;
        this.frmaeY = 0;
        this.spriteWidth = 200;
        this.spriteHeight = 200;
        this.minFrame = 0;
        this.maxFrame = 4;
        this.choosenDefender = choosenDefender;
    }
    draw(){
        //ctx.fillStyle = 'blue';
        //ctx.fillRect(this.x, this.y, this.width, this.height);
        contxt.fillStyle = 'gold';
        contxt.font = '30px Orbitron';
        contxt.fillText(Math.floor(this.health), this.x + 15, this.y + 30);

        if (this.choosenDefender ===1){
            contxt.drawImage(defender1, this.frameX * this.spriteWidth, 0, this.spriteWidth, this.spriteHeight, this.x, this.y, this.width, this.height);
        } else if (this.choosenDefender === 2){
            contxt.drawImage(defender2, this.frameX * this.spriteWidth, 0, this.spriteWidth, this.spriteHeight, this.x, this.y, this.width, this.height);
        }
        
    }
    update(){
        if(frame % 8 === 0){
            if(this.frameX < this.maxFrame) this.frameX++;
            else this.frameX = this.minFrame;
            if(this.frameX === 15) this.shootNow =  true
        }

        if (this.shooting){
            this.timer++;
            if (this.timer % 100 === 0){
                projectiles.push(new Projectile(this.x + 70, this.y + 50));
            }
        } else {
            this.timer = 0;
        }
    }
}
canvas.addEventListener('click', function(){
    const gridPositionX = mouse.x  - (mouse.x % cellSize) + cellGap;
    const gridPositionY = mouse.y - (mouse.y % cellSize) + cellGap;
    if (gridPositionY < cellSize) return;
    for (let i = 0; i < defenders.length; i++){
        if (defenders[i].x === gridPositionX && defenders[i].y === gridPositionY) return;
    }
    let defenderCost = 100;
    if (numberOfResources >= defenderCost){
        defenders.push(new Defender(gridPositionX, gridPositionY));
        numberOfResources -= defenderCost;
    }
});
function handleDefenders(){
    for (let i = 0; i < defenders.length; i++){
        defenders[i].draw();
        defenders[i].update();
        if (enemyPositions.indexOf(defenders[i].y) !== -1){
            defenders[i].shooting = true;
        } else {
            defenders[i].shooting = false;
        }
        for (let j = 0; j < enemies.length; j++){
            if (defenders[i] && collision(defenders[i], enemies[j])){
                enemies[j].movement = 0;
                defenders[i].health -= 1;
            }
            if (defenders[i] && defenders[i].health <= 0){
                defenders.splice(i, 1);
                i--;
                enemies[j].movement = enemies[j].speed;
            }
        }
    }
}

const card1 = {
    x: 10,
    y: 10,
    width: 70,
    height: 85
}

const card2 = {
    x: 90,
    y: 10,
    width: 70,
    height: 85
}

function chooseDefender(){
    let card1stroke = 'black';
    let card2stroke = 'black';
    if(collision(mouse, card1) && mouse.clicked){
        choosenDefender = 1;
    } else if (collision(mouse, card2)&& mouse.clicked){
        choosenDefender = 2;
    }
    if (choosenDefender === 1){
        card1stroke = 'gold';
        card2stroke = 'black';
    } else if (choosenDefender ===2){
        card1stroke = 'black';
        card2stroke = 'gold';
    } else {
        card1stroke = 'black';
        card2stroke = 'black';

    }

    contxt.lineWidth = 1;
    contxt.fillStyle = 'rgba(0,0,0,0.2)';
    contxt.fillRect(card1.x, card1.y, card1.width, card1.height);
    contxt.strokeStyle = card1stroke;
    contxt.strokeRect(card1.x, card1.y, card1.width, card1.height);
    contxt.drawImage(defender1, 0, 0, 200, 200, 0, 5, 200/2, 200/2);
    contxt.fillRect(card2.x, card2.y, card2.width, card2.height);
    contxt.strokeStyle = card2stroke;
    contxt.drawImage(defender2, 0, 0, 200, 200, 75, 5, 200/2, 200/2);
    contxt.strokeRect(card2.x, card2.y, card2.width, card2.height);

}

// enemies
const enemyTypes = [];
const enemy1 = new Image();
enemy1.src = 'Attack3.png';
enemyTypes.push(enemy1);
const enemy2 = new Image();
enemy2.src = 'Attack2.png';
enemyTypes.push(enemy2);

class Enemy {
    constructor(verticalPosition){
        this.x = canvas.width;
        this.y = verticalPosition;
        this.width = cellSize - cellGap * 2;
        this.height = cellSize - cellGap * 2;
        this.speed = Math.random() * 0.2 + 0.4;
        this.movement = this.speed;
        this.health = 100;
        this.maxHealth = this.health;
        this.enemyType = enemyTypes[Math.floor(Math.random() * enemyTypes.length)];
        this.frameX = 0;
        this.frmaeY = 0;
        this.minFrame = 0;
        this.maxFrame = 5;
        this.spriteWidth = 149;
        this.spriteHeight = 149;

    }
    update(){
        this.x -= this.movement;
        if (frame % 9 === 0){
            if (this.frameX < this.maxFrame) this.frameX++;
            else this.frameX = this.minFrame;
        }
    }
    draw(){
        //ctx.fillStyle = 'red';
        //ctx.fillRect(this.x, this.y, this.width, this.height);
        contxt.fillStyle = 'white';
        contxt.font = '30px Orbitron';
        contxt.fillText(Math.floor(this.health), this.x + 15, this.y + 30);
        contxt.drawImage(this.enemyType, this.frameX * this.spriteWidth, 0, this.spriteWidth, this.spriteHeight, this.x, this.y, this.width, this.height);
    }
}
function handleEnemies(){
    for (let i = 0; i < enemies.length; i++){
        enemies[i].update();
        enemies[i].draw();
        if (enemies[i].x < 0){
            gameOver = true;
        }
        if (enemies[i].health <= 0){
            let gainedResources = enemies[i].maxHealth/10;
            numberOfResources += gainedResources;
            score += gainedResources;
            const findThisIndex = enemyPositions.indexOf(enemies[i].y);
            enemyPositions.splice(findThisIndex, 1);
            enemies.splice(i, 1);
            i--;
          }
    }
    if (frame % enemiesInterval === 0 && score < winningScore){
        let verticalPosition = Math.floor(Math.random() * 5 + 1) * cellSize + cellGap;
        enemies.push(new Enemy(verticalPosition));
        enemyPositions.push(verticalPosition);
        if (enemiesInterval > 120) enemiesInterval -= 50;
    }
}

// resources
const amounts = [20, 30, 40];
class Resource {
    constructor(){
        this.x = Math.random() * (canvas.width - cellSize);
        this.y = (Math.floor(Math.random() * 5) + 1) * cellSize + 25;
        this.width = cellSize * 0.6;
        this.height = cellSize * 0.6;
        this.amount = amounts[Math.floor(Math.random() * amounts.length)];
    }
    draw(){
        contxt.fillStyle = 'yellow';
        contxt.fillRect(this.x, this.y, this.width, this.height);
        contxt.fillStyle = 'black';
        contxt.font = '20px Orbitron';
        contxt.fillText(this.amount, this.x + 15, this.y + 25);
    }
}
function handleResources(){
    if (frame % 500 === 0 && score < winningScore){
        resources.push(new Resource());
    }
    for (let i = 0; i < resources.length; i++){
        resources[i].draw();
        if (resources[i] && mouse.x && mouse.y && collision(resources[i], mouse)){
            numberOfResources += resources[i].amount;
            resources.splice(i, 1);
            i--;
        }
    }
}

// utilities
function handleGameStatus(){
    contxt.fillStyle = 'gold';
    contxt.font = '30px Orbitron';
    contxt.fillText('Score: ' + score, 180, 40);
    contxt.fillText('Resources: ' + numberOfResources, 180, 80);
    if (gameOver){
        contxt.fillStyle = 'gold';
        contxt.font = '90px Orbitron';
        contxt.fillText('GAME OVER', 135, 330);
    }
    if (score >= winningScore && enemies.length === 0){
        contxt.fillStyle = 'black';
        contxt.font = '60px Orbitron';
        contxt.fillText('LEVEL COMPLETE', 130, 300);
        contxt.font = '30px Orbitron';
        contxt.fillText('You win with ' + score + ' points!', 134, 340);
    }
}

function animate(){
    contxt.clearRect(0, 0, canvas.width, canvas.height);
    contxt.fillStyle = 'black';
    contxt.fillRect(0,0,controlsBar.width, controlsBar.height);
    handleGameGrid();
    handleDefenders();
    handleResources();
    handleProjectiles();
    handleEnemies();
    chooseDefender();
    handleGameStatus();
    frame++;
    if (!gameOver) requestAnimationFrame(animate);
}
animate();

function collision(first, second){
    if (    !(  first.x > second.x + second.width ||
                first.x + first.width < second.x ||
                first.y > second.y + second.height ||
                first.y + first.height < second.y)
    ) {
        return true;
    };
};

window.addEventListener('resize', function(){
    canvasPosition = canvas.getBoundingClientRect();
})