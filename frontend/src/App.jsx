import { StateSelect } from "./components/common/SelectField";
import { EnergyInput } from "./components/common/NumberInput";

function App() {
  return (
    <div className="flex flex-col items-center justify-center gap-6 h-screen">
      <StateSelect />
      <EnergyInput />
    </div>
  );
}

export default App;
