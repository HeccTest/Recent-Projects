const canvas = document.getElementById('canvas') // canvas reference name
const c = canvas.getContext("2d")

c.fillRect(0, 0, canvas.width, canvas.height)

const gravity = 0.2

class sprite {
  constructor({position, velocity}) { // take in two objects
    this.position = position
    this.velocity = velocity
    this.height = 150
    this.lastKey
  }

  draw() {
    c.fillStyle = 'red'
    c.fillRect(this.position.x, this.position.y, 50, this.height)
  }

  update() {
    this.draw() // draw a new sprite every frame
    this.position.x += this.velocity.x
    this.position.y += this.velocity.y // constatntly change position by velocity

    if(this.position.y + this.height + this.velocity.y >= canvas.height)
    {
      this.velocity.y = 0
    }
    else {
      this.velocity.y += gravity
    }
  }
}

const player = new sprite({
  position: {
    x: 0,
    y: 0
  },
  velocity: {
    x: 0,
    y: 0
  }
})

const enemy = new sprite({
  position: {
    x: 974,
    y: 0
  },
  velocity: {
    x: 0,
    y: 0
  }
})

console.log(player)

const keys = {
  a: {
    pressed: false
  },
  d: {
    pressed: false
  },
  ArrowLeft: {
    pressed: false
  },
  ArrowRight: {
    pressed: false
  }
}

function animation() {
  window.requestAnimationFrame(animation) // infinite (nested) loop
  c.fillStyle = 'black'
  c.fillRect(0, 0, canvas.width, canvas.height)
  player.update()
  enemy.update()

  player.velocity.x = 0 // always set player x velocity to 0
  enemy.velocity.x = 0 // ^

  // player movement
  if(keys.a.pressed == true && player.lastKey === 'a') // strict equality (===) ensures the compared items are of the same type
  {
    player.velocity.x = -5
  }
  else if(keys.d.pressed == true && player.lastKey === 'd')
  {
    player.velocity.x = 5
  }

  // enemy movement
  if(keys.ArrowLeft.pressed == true && enemy.lastKey === 'ArrowLeft')
  {
    enemy.velocity.x = -5
  }
  else if(keys.ArrowRight.pressed == true && enemy.lastKey === 'ArrowRight')
  {
    enemy.velocity.x = 5
  }
}
animation()


window.addEventListener('keydown', (event) => {
  console.log(event.key)
  switch(event.key){
    case 'd':
      keys.d.pressed = true
      player.lastKey = 'd'
      break
    case 'a':
      keys.a.pressed = true
      player.lastKey = 'a'
      break
    case 'w':
      if(player.velocity.y == 0) // prevents player from jumping in the air. Enemy can jump indefinitely
      {
        player.velocity.y = -10;
      }
      break

    case 'ArrowRight':
      keys.ArrowRight.pressed = true
      enemy.lastKey = 'ArrowRight'
      break
    case 'ArrowLeft':
      keys.ArrowLeft.pressed = true
      enemy.lastKey = 'ArrowLeft'
      break
    case 'ArrowUp':
      enemy.velocity.y = -10;
      break
  }
})

window.addEventListener('keyup', (event) => {
  switch(event.key){
    case 'd': // let go of d
      keys.d.pressed = false
      break
    case 'a': // let go of a
      keys.a.pressed = false
      break

    case 'ArrowLeft': // let go of ArrowLeft
      keys.ArrowLeft.pressed = false
      break
    case 'ArrowRight': // let go of ArrowRight
      keys.ArrowRight.pressed = false
      break
  }
})
