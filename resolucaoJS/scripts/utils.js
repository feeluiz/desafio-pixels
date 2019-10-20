export default  {
    carregarCanvas(canvas){
        //pega o dom do canvas
        var canvas = document.querySelector(canvas);

        //retorna o contexto 2d caso o objeto seja valido
        if(canvas && canvas.getContext){
           var contexto = canvas.getContext('2d');
           if(contexto) return contexto;
        }
        return FALSE;
     },
     init() {
            //pega o contexto
            var contexto = this.carregarCanvas("#canvas")
            var result = document.querySelector('#result');
            if(contexto){
                //cria a imagem
                var image = new Image();
                image.onload = async () => {
                    //desenha a imagem no canas
                    contexto.drawImage(image, 0, 0);
                    //pega os todos os pixels da imagem pra um array
                    const imageData = await contexto.getImageData(0, 0, image.width, image.height);
                    //troca as cores e conta quanto pixels veremlhos existem
                    result.innerText = this.changeColors(imageData.data);   
                    //altera a cor das posicoes alterados no cavans          
                    await contexto.putImageData(imageData, 0, 0);
                }
                //caminho da imagem
                image.src = 'img/img.png';
            }
    },
    changeColors(data) {
        //contador
        var count = 0

        //percorre o array Uint8ClampedArray conta pixels
        // e altera a cor
        for (var i = 0; i <= data.length; i+=4) {
            if(data[i] == 255 && data[i+1] == 0 && data[i+2] == 0){
                data[i + 2] = 255;//rosa
                count++;
            }else if(data[i] == 0 && data[i+1] == 0 && data[i+2] == 0){
                data[i + 1] = 255; //verde
            }
        }
        //retorna o contador
        return `O total de pixels vermelhos eh: ${count}`;
    }
}