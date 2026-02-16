import { StateSelect } from "./components/common/SelectField";
import { EnergyInput } from "./components/common/NumberInput";
import { WithAvatar } from "./components/common/Card";
import { ButtonSearch } from "./components/common/Button";
import { Surface } from "@heroui/react";
import { Separator } from "@heroui/react";

function App() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50">
      <Surface
        className="flex min-w-[320px] flex-col gap-3 rounded-3xl border p-6"
        variant="transparent"
      >
        <div className="flex gap-10 items-start">
          <div className="flex flex-col gap-6">
            <StateSelect />
            <EnergyInput />
            <ButtonSearch />
            <Separator className="my-4" />
          </div>

          <WithAvatar />
        </div>
      </Surface>
    </div>
  );
}

export default App;
