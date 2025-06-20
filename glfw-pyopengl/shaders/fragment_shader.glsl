#version 330 core

out vec4 FragColor; // cor que será saída do fragment shader

uniform float red;

void main()
{
    FragColor = vec4(red, 0.5, 0.3, 1.0); // vermelho sólido (RGBA)
}
