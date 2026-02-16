export function getSolucaoStyle(tipo) {
  if (tipo === "Geração Distribuída") {
    return "bg-teal-50 text-teal-600 border-teal-200";
  }

  if (tipo === "Mercado Livre") {
    return "bg-cyan-50 text-cyan-600 border-cyan-200";
  }

  return "bg-gray-50 text-gray-600 border-gray-200";
}
