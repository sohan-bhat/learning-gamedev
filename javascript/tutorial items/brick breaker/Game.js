import Paddle from './Paddle.js'
import InputHandler from './Input.js'
import Ball from './Ball.js'
import Brick from './Brick.js'

export default class Game {
    constructor(gameWidth, gameHeight) {
        this.gameWidth = gameWidth
        this.gameHeight = gameHeight
    }

    start() {
        this.ball = new Ball(this)
        this.paddle = new Paddle(this)

        let bricks = []
        for (let i = 0; i < 10; i++) {
            bricks.push(new Brick(this, { x: i * 52, y: 30}))
        }

        this.gameObjects = [
            this.ball,
            this.paddle,
            ...bricks
        ]

        new InputHandler(this.paddle)
    }


    update(deltaTime) {
        this.gameObjects.forEach(object => object.update(deltaTime))
    }

    draw(ctx) {
        this.gameObjects.forEach(object => object.draw(ctx))
    }
}