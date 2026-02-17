// Palabra.jsx - El ladrillo de la Misión SADV41
export const Palabra = ({ index }) => {
  const identity = [
    "Redimido", "Neutrino", "Ebenezer", 
    "Santisimo", "Consumado", "Trueno", "SADV41"
  ];
  
  // Devuelve la palabra solicitada envuelta en la protección del Padre
  return <span className={`identity-${index}`}>{identity[index]}</span>;
};
