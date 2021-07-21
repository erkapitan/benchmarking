import unittest

from famapy.metamodels.fm_metamodel.transformations.xml_transformation import XMLTransformation

from famapy.metamodels.pysat_metamodel.transformations.fm_to_pysat import FmToPysat
from famapy.metamodels.pysat_metamodel.models.pysat_model import PySATModel
from famapy.metamodels.pysat_metamodel.operations.glucose3_products_number import Glucose3ProductsNumber


class ProductsNumberTest(unittest.TestCase):

    def ProductsOperation(self, model: PySATModel, expected_output: bool):
        products_operation = Glucose3ProductsNumber()

        products_operation.execute(model)
        products = products_operation.get_products_number()

        self.assertEqual(products, expected_output)

    def load_model(self, model_path):
        xmlreader = XMLTransformation(model_path)
        fm = xmlreader.transform()

        transform = FmToPysat(fm)
        return transform.transform()

    def testCaseMandatory(self):
        pysat_model = self.load_model("models/fama_test_suite/relationships/mandatory/mandatory.xml")
        expected_output = 1
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseOptional(self):
        pysat_model = self.load_model("models/fama_test_suite/relationships/optional/optional.xml")
        expected_output = 2
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseAlternative(self):
        pysat_model = self.load_model("models/fama_test_suite/relationships/alternative/alternative.xml")
        expected_output = 2
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseOr(self):
        pysat_model = self.load_model("models/fama_test_suite/relationships/or/or.xml")
        expected_output = 3
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseExcludes(self):
        pysat_model = self.load_model("models/fama_test_suite/relationships/excludes/excludes.xml")
        expected_output = 3
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseRequires(self):
        pysat_model = self.load_model("models/fama_test_suite/relationships/requires/requires.xml")
        expected_output = 3
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseMandatoryOptional(self):
        pysat_model = self.load_model("models/fama_test_suite/relationships/mandatory-optional/mandatory-optional.xml")
        expected_output = 4
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseMandatoryOr(self):
        pysat_model = self.load_model("models/fama_test_suite/relationships/mandatory-or/mandatory-or.xml")
        expected_output = 9
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseMandatoryAlternative(self):
        pysat_model = self.load_model("models/fama_test_suite/relationships/mandatory-alternative/mandatory-alternative.xml")
        expected_output = 4
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseMandatoryRequires(self):
        pysat_model = self.load_model("models/fama_test_suite/relationships/mandatory-requires/mandatory-requires.xml")
        expected_output = 1
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseMandatoryExcludes(self):
        pysat_model = self.load_model("models/fama_test_suite/relationships/mandatory-excludes/mandatory-excludes.xml")
        expected_output = 0
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseOptionalOr(self):
        pysat_model = self.load_model("models/fama_test_suite/relationships/optional-or/optional-or.xml")
        expected_output = 20
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseOptionalAlternative(self):
        pysat_model = self.load_model("models/fama_test_suite/relationships/optional-alternative/optional-alternative.xml")
        expected_output = 9
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseOrAlternative(self):
        pysat_model = self.load_model("models/fama_test_suite/relationships/or-alternative/or-alternative.xml")
        expected_output = 20
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseOrRequires(self):
        pysat_model = self.load_model("models/fama_test_suite/relationships/or-requires/or-requires.xml")
        expected_output = 2
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseOrExcludes(self):
        pysat_model = self.load_model("models/fama_test_suite/relationships/or-excludes/or-excludes.xml")
        expected_output = 2
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseAlternativeRequires(self):
        pysat_model = self.load_model("models/fama_test_suite/relationships/alternative-requires/alternative-requires.xml")
        expected_output = 1
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseAlternativeExcludes(self):
        pysat_model = self.load_model("models/fama_test_suite/relationships/alternative-excludes/alternative-excludes.xml")
        expected_output = 2
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseRequiresExcludes(self):
        pysat_model = self.load_model("models/fama_test_suite/relationships/requires-excludes/requires-excludes.xml")
        expected_output = 2
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseAllRelationships(self):
        pysat_model = self.load_model("models/fama_test_suite/relationships/allrelationships/allrelationships.xml")
        expected_output = 4
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseAlternativeOddChildren(self):
        pysat_model = self.load_model("models/fama_test_suite/refinement/alternative-oddChildren/alternative-oddChildren.xml")
        expected_output = 0
        self.ProductsOperation(pysat_model, expected_output)


if __name__ == '__main__':
    unittest.main()
