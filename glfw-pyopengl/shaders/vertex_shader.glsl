#version 330 core

layout(location = 0) in vec2 aPos; // recebe posição do vértice (x,y)

uniform vec2 u_position;
uniform float scale; // variável para controlar a escala

void main()
{
    vec2 scaledPos = aPos * scale; // aplica a escala
    gl_Position = vec4(scaledPos + u_position, 0.0, 1.0); // coloca a posição no formato vec4, com z=0 e w=1
}
